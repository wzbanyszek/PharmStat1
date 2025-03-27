import streamlit as st
from utils.translations import translations

# Konfiguracja strony
st.set_page_config(page_title="Santo Pharmstat", layout="wide")

# Wybór języka
language = st.sidebar.selectbox(
    "Wybierz język / Select Language / Выберите язык",
    options=["Polski", "English", "Русский"],
    index=0  # Ustawienie domyślnego języka (0 = Polski, 1 = English, 2 = Русский)
)

# Ustawienie tłumaczeń na podstawie wybranego języka
t = translations[language]

# Menu boczne
st.sidebar.title(t["general"]["menu_title"])
page = st.sidebar.radio(
    t["general"]["choose_page"],
    [
        t["general"]["intro"],
        t["descriptive_statistics"]["descriptive_stats"],
        #t["histogram_analysis"]["histograms"],
        #t["boxplot_charts"]["boxplot"],
        t["control_charts"]["control_charts"],
        t["process_capability"]["process_capability"],
        t["stability_regression"]["stability_regression"]
        #t["temp_humidity_analysis"]["temp_humidity"],
        #t["pqr_module"]["title"]  
    ]
)

# Routing podstron
if page == t["general"]["intro"]:
    from AppPages import Wprowadzenie
    Wprowadzenie.show(language)

elif page == t["descriptive_statistics"]["descriptive_stats"]:
    from AppPages import descriptive_statistics
    descriptive_statistics.show(language)

elif page == t["histogram_analysis"]["histograms"]:
    from AppPages import histogram_analysis
    histogram_analysis.show(language)

elif page == t["boxplot_charts"]["boxplot"]:
    from AppPages import BoxPlot
    BoxPlot.show(language)

elif page == t["control_charts"]["control_charts"]:
    from AppPages import control_charts
    control_charts.show(language)

elif page == t["process_capability"]["process_capability"]:
    from AppPages import process_capability
    process_capability.show(language)

elif page == t["stability_regression"]["stability_regression"]:
    from AppPages import stability_analysis
    stability_analysis.show(language)

elif page == t["temp_humidity_analysis"]["temp_humidity"]:
    from AppPages import Analiza_temperatury_wilgotnosci
    Analiza_temperatury_wilgotnosci.show(language)

elif page == t["pqr_module"]["title"]:  
    from AppPages import pqr
    pqr.show(language)
