import streamlit as st
from utils.translations import translations

def show(language):
    t = translations[language]

    st.header(t["general"]["intro"])
    st.write(f"""
    {t["general"]["intro_desc"]}

    **{t["general"]["menu_title"]}:**

    1. **{t["descriptive_statistics"]["descriptive_stats"]}**  
       {t["descriptive_statistics"]["descriptive_stats_desc"]}

    2. **{t["control_charts"]["control_charts"]}**  
       {t["control_charts"]["control_charts_desc"]}

    3. **{t["process_capability"]["process_capability"]}**  
       {t["process_capability"]["process_capability_desc"]}

    4. **{t["stability_regression"]["stability_regression"]}**  
       {t["stability_regression"]["stability_regression_desc"]}

    ---
    **{t["general"]["how_to_use"]}**  
    - {t["general"]["choose_page"]}
    - {t["general"]["upload_data"]}
    - {t["general"]["view_results"]}
    - {t["general"]["customize_view"]}
    """)
