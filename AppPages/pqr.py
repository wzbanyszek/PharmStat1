import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from SPC import ImRControlChart, Rule01, Rule02, Rule03, Rule04, Rule05, Rule06, Rule07, Rule08
from utils.translations import translations

def show(language):
    t = translations[language]["pqr_module"]

    st.header(t["title"])

    st.write(f"""
    **{t["instructions"]["header"]}:**
    - {t["instructions"]["upload_file"]}
    - {t["instructions"]["select_series"]}
    - {t["instructions"]["input_spec_limits"]}
    - {t["instructions"]["view_charts"]}
    """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            col_count = df.shape[1]
            if col_count < 2:
                st.error(t["file_handling"]["error_two_columns"])
                return

            df.rename(columns={df.columns[0]: t["chart_labels"]["time_series"]}, inplace=True)

            if col_count > 2:
                result_column = st.selectbox(
                    t["file_handling"]["select_result_column"],
                    df.columns[1:],
                    help=t["file_handling"]["select_result_column_help"]
                )
            else:
                result_column = df.columns[1]

            df[t["chart_labels"]["values"]] = df[result_column]

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(df[[t["chart_labels"]["time_series"], t["chart_labels"]["values"]]].head(10))

            df[t["chart_labels"]["time_series"]] = df[t["chart_labels"]["time_series"]].astype(str)
            df[t["chart_labels"]["values"]] = pd.to_numeric(df[t["chart_labels"]["values"]], errors='coerce')
            df.dropna(subset=[t["chart_labels"]["values"]], inplace=True)

            if df.empty:
                st.error(t["file_handling"]["error_no_numeric_data"])
                return

            data_array = df[t["chart_labels"]["values"]].to_numpy().reshape(-1, 1)
            series_ids = df[t["chart_labels"]["time_series"]].to_list()

            # Karta kontrolna ImR
            st.subheader(t["subheaders"]["imr_chart"])
            chart = ImRControlChart(
                data=data_array,
                xlabel=t["chart_labels"]["observation"],
                ylabel_top=t["chart_labels"]["individual_values"],
                ylabel_bottom=t["chart_labels"]["moving_range"]
            )

            chart.limits = True
            chart.append_rules([
                Rule01(), Rule02(), Rule03(), Rule04(),
                Rule05(), Rule06(), Rule07(), Rule08()
            ])

            chart.plot()
            fig = plt.gcf()
            st.pyplot(fig)

            # Analiza zdolności procesowej Cpk z histogramem
            st.subheader(t["subheaders"]["cpk_analysis"])
            usl = st.number_input(t["spec_limits"]["usl"], value=0.0)
            lsl = st.number_input(t["spec_limits"]["lsl"], value=0.0)

            if usl == lsl:
                st.warning(t["warnings"]["spec_limits_equal"])
            else:
                mean = np.mean(data_array)
                std_dev = np.std(data_array, ddof=1)
                cpk = min((usl - mean) / (3 * std_dev), (mean - lsl) / (3 * std_dev))

                fig, ax = plt.subplots(figsize=(10, 6))
                n, bins, patches = ax.hist(data_array, bins=20, density=True, alpha=0.6, color='g', edgecolor='black')

                y = norm.pdf(bins, mean, std_dev)
                ax.plot(bins, y, '--', color='black')

                ax.axvline(usl, color='r', linestyle='dashed', linewidth=2, label=t["spec_limits"]["usl"])
                ax.axvline(lsl, color='b', linestyle='dashed', linewidth=2, label=t["spec_limits"]["lsl"])

                ax.set_xlabel(t["chart_labels"]["values"])
                ax.set_ylabel(t["chart_labels"]["frequency"])
                ax.set_title(t["chart_labels"]["histogram_with_spec_limits"])
                ax.legend()

                st.pyplot(fig)
                st.write(f"{t['cpk_results']['mean']}: **{mean:.2f}**")
                st.write(f"{t['cpk_results']['std_dev']}: **{std_dev:.2f}**")
                st.write(f"{t['cpk_results']['cpk']}: **{cpk:.2f}**")

            # Wykres porównujący wyniki z limitami specyfikacji
            st.subheader(t["subheaders"]["spec_limits_comparison"])
            fig, ax = plt.subplots(figsize=(12, 6))
            ax.plot(series_ids, data_array, marker='o', linestyle='-', label=t["chart_labels"]["values"])
            ax.axhline(usl, color='r', linestyle='dashed', linewidth=2, label=t["spec_limits"]["usl"])
            ax.axhline(lsl, color='r', linestyle='dashed', linewidth=2, label=t["spec_limits"]["lsl"])
            ax.set_xlabel(t["chart_labels"]["time_series"])
            ax.set_ylabel(t["chart_labels"]["values"])
            ax.set_title(t["chart_labels"]["control_chart_with_spec_limits"])
            plt.xticks(rotation=45)
            plt.grid(True)
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
