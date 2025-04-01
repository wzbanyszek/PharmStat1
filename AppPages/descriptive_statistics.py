import streamlit as st
import pandas as pd
from scipy.stats import shapiro, skew, kurtosis
from utils.data_processing import calculate_descriptive_stats
from utils.translations import translations

def show(language):
    t = translations[language]["descriptive_statistics"]

    st.header(t["title"])

    st.write(f"""
    **{t["instructions"]["header"]}:**
    - {t["instructions"]["upload_file"]}
    - {t["instructions"]["select_columns"]}
    - {t["instructions"]["stats_summary"]}
    - {t["instructions"]["normality_skew_kurtosis"]}
    """)

    # Wczytywanie pliku
    uploaded_file = st.file_uploader(t["file_handling"]["choose_file"], type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)

            # Podgląd danych z możliwością włączania i wyłączania
            show_data = st.checkbox(t["file_handling"]["show_data_preview"], value=True)
            if show_data:
                st.write(f"**{t['file_handling']['data_preview']}**")
                st.dataframe(df.head())

            columns = df.columns.tolist()
            selected_columns = st.multiselect(
                t["file_handling"]["select_columns"],
                columns,
                default=columns
            )

            if selected_columns:
                st.subheader(t["title"])
                stats = calculate_descriptive_stats(df[selected_columns])

                # Dodanie wyników testu normalności, skośności i kurtozy jako wierszy
                additional_stats = {}
                for column in selected_columns:
                    data = df[column].dropna()
                    stat, p_value = shapiro(data)
                    skewness = skew(data)
                    kurt = kurtosis(data)

                    #additional_stats.setdefault(t["statistics"]["shapiro_test"], []).append(round(p_value, 4))
                    additional_stats.setdefault(t["statistics"]["skewness"], []).append(round(skewness, 2))
                    additional_stats.setdefault(t["statistics"]["kurtosis"], []).append(round(kurt, 2))

                # Konwersja dodatkowych wyników do DataFrame
                additional_stats_df = pd.DataFrame(additional_stats, index=selected_columns).T

                # Łączenie statystyk opisowych z dodatkowymi statystykami
                full_stats = pd.concat([stats, additional_stats_df])

                st.dataframe(full_stats)

        except Exception as e:
            st.error(f"{t['file_handling']['error_processing_file']}: {e}")
    else:
        st.info(t["file_handling"]["no_file_uploaded"])
