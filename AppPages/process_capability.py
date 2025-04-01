import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from utils.translations import translations


def show(language):
    t = translations[language]["process_capability"]

    st.header(t["title"])

    st.write(f"""
    **{t["instructions"]["header"]}:**
    - {t["instructions"]["upload_file"]}
    - {t["instructions"]["set_spec_limits"]}
    - {t["instructions"]["view_results"]}
    """)

    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            columns = df.columns.tolist()

            selected_column = st.selectbox(t["file_handling"]["select_column"], columns)

            data = df[selected_column].dropna()

            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.subheader(t["file_handling"]["data_preview"])
                st.dataframe(data.head(10))

            st.subheader(t["spec_settings"]["target"])
            #target = st.number_input(t["spec_settings"]["target"], value=float(data.mean()))
            #LSL = st.number_input(t["spec_settings"]["lsl"], value=float(data.min()))
            #USL = st.number_input(t["spec_settings"]["usl"], value=float(data.max()))
            target = st.number_input(t["spec_settings"]["target"], value=0.0, format="%0.01f")
            LSL = st.number_input(t["spec_settings"]["lsl"], value=0.0, format="%0.01f")
            USL = st.number_input(t["spec_settings"]["usl"], value=0.0, format="%0.01f")

            x = np.linspace(min(data), max(data), 1000)
            y = norm.pdf(x, loc=target, scale=data.std())

            plt.figure(figsize=(15, 10))
            plt.hist(data, color="lightgrey", edgecolor="black", density=True, label="Histogram danych")
            sns.kdeplot(data, color="blue", label="Gęstość danych")
            plt.plot(x, y, linestyle="--", color="black", label="Teoretyczna gęstość (Normalna)")
            plt.axvline(LSL, linestyle="--", color="red", label="LSL")
            plt.axvline(USL, linestyle="--", color="orange", label="USL")
            plt.axvline(target, linestyle="--", color="green", label="Target")
            plt.title(t["plot"]["title"])
            plt.xlabel(t["plot"]["x_label"])
            plt.ylabel(t["plot"]["y_label"])
            plt.yticks([])
            plt.legend()
            st.pyplot(plt.gcf())

            Cp = (USL - LSL) / (6 * data.std())
            Cpk = min((USL - data.mean()) / (3 * data.std()), (data.mean() - LSL) / (3 * data.std()))

            num_samples = len(data)
            sample_mean = data.mean()
            sample_std = data.std()
            sample_max = data.max()
            sample_min = data.min()
            sample_median = np.median(data)

            pct_below_LSL = len(data[data < LSL]) / len(data) * 100
            pct_above_USL = len(data[data > USL]) / len(data) * 100

            st.subheader(t["results"]["header"])

            st.write(f"**{t["results"]["cp"]}:** {round(Cp, 2)}")
            st.write(f"**{t["results"]["cpk"]}:** {round(Cpk, 2)}")

            st.write("---")
            st.write(f"**{t["results"]["sample_size"]}:** {num_samples}")
            st.write(f"**{t["results"]["sample_mean"]}:** {round(sample_mean, 2)}")
            st.write(f"**{t["results"]["sample_std"]}:** {round(sample_std, 2)}")
            st.write(f"**{t["results"]["sample_max"]}:** {sample_max}")
            st.write(f"**{t["results"]["sample_min"]}:** {sample_min}")
            st.write(f"**{t["results"]["sample_median"]}:** {sample_median}")

            st.write(f"**{t["results"]["pct_below_lsl"]}:** {round(pct_below_LSL, 2)}%")
            st.write(f"**{t["results"]["pct_above_usl"]}:** {round(pct_above_USL, 2)}%")

        except Exception as e:
            st.error(f"{t["file_handling"]["error_processing_file"]}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
