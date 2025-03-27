translations = {
    "Polski": {
        "general": {
            "menu_title": "Menu",
            "intro": "Witaj w aplikacji Santo Pharmstat!",
            "intro_desc": "Aplikacja umożliwia przeprowadzanie analizy danych statystycznych i jakościowych w prosty i intuicyjny sposób. W bocznym menu znajdziesz moduły, które pomogą Ci w analizie danych z różnych perspektyw.",
            "choose_page": "Wybierz podstronę:",
            "upload_data": "Wczytaj dane do analizy przy pomocy wbudowanych formularzy.",
            "view_results": "Wyniki analizy (wykresy, tabele, statystyki) pojawią się w głównym obszarze strony.",
            "customize_view": "Możesz ukrywać lub wyświetlać szczegóły analizy, dostosowując widok do swoich potrzeb.",
            "how_to_use": "Jak korzystać z aplikacji?"
        },
        "descriptive_statistics": {
            "descriptive_stats": "Statystyki opisowe",
            "descriptive_stats_desc": "Obliczanie podstawowych statystyk, takich jak średnia, mediana, odchylenie standardowe. Moduł ten pozwala na szybkie i łatwe uzyskanie podstawowych informacji o Twoich danych, co jest kluczowe dla dalszej analizy. Statystyki opisowe są fundamentem analizy danych, ponieważ umożliwiają szybkie zrozumienie rozkładu i zmienności danych.",
            "title": "Statystyki opisowe",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny, dla których chcesz obliczyć statystyki opisowe.",
                "stats_summary": "Otrzymasz zestawienie najważniejszych statystyk, takich jak średnia, mediana, odchylenie standardowe i inne.",
                "normality_skew_kurtosis": "Dodatkowo ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd wczytanych danych",
                "data_preview": "Podgląd wczytanych danych (pierwsze 10 wierszy):",
                "select_columns": "Wybierz kolumny do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "shapiro_test": "Shapiro-Wilk p-wartość",
                "skewness": "Skośność",
                "kurtosis": "Kurtoza"
            }
        },
        "histogram_analysis": {
            "histograms": "Histogramy",
            "histograms_desc": "Tworzenie histogramów z oceną normalności rozkładu i analizą skośności oraz kurtozy. Dzięki temu modułowi możesz wizualizować rozkład swoich danych i ocenić, czy mają one charakterystykę rozkładu normalnego. Histogramy są użytecznym narzędziem do identyfikacji kształtu rozkładu danych oraz do wykrywania ewentualnych odchyleń lub anomalii.",
            "title": "Analiza histogramów",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_column": "Wybierz kolumnę do analizy, aby wygenerować histogram i wyświetlić statystyki opisowe.",
                "normality_test": "Ocenisz normalność rozkładu oraz uzyskasz informacje o skośności i kurtozie."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_column": "Wybierz kolumnę do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "sample_size": "Liczba próbek",
                "mean": "Średnia",
                "std_dev": "Odchylenie standardowe",
                "max": "Maksimum",
                "min": "Minimum",
                "median": "Mediana",
                "rsd": "Współczynnik zmienności (RSD %)",
                "shapiro_test": "Test Shapiro-Wilka",
                "skewness": "Skośność",
                "kurtosis": "Kurtoza"
            },
            "plot": {
                "histogram_title": "Histogram danych",
                "x_label": "Wartości",
                "y_label": "Częstość"
            },
            "normality_results": {
                "normal_distribution": "Brak podstaw do odrzucenia hipotezy o normalności rozkładu.",
                "non_normal_distribution": "Dane nie pochodzą z rozkładu normalnego."
            }
        },
        "boxplot_charts": {
            "boxplot": "Wykresy pudełkowe BoxPlot",
            "boxplot_desc": "Wizualizacja rozkładu danych i identyfikacja wartości odstających. Wykresy pudełkowe umożliwiają szybkie zrozumienie rozkładu danych, pokazując medianę, kwartyle oraz wartości odstające. Są one szczególnie przydatne w identyfikacji potencjalnych błędów pomiarowych lub nietypowych obserwacji.",
            "title": "Wykresy BoxPlot",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "select_columns": "Wybierz kolumny do analizy, aby wygenerować wykresy BoxPlot.",
                "view_stats": "Otrzymasz statystyki opisowe dla wybranych kolumn."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx, xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 5 wierszy):",
                "select_columns": "Wybierz kolumny do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "plot": {
                "title": "Wykresy BoxPlot dla wybranych kolumn",
                "y_label": "Wartości"
            },
            "statistics": {
                "title": "Statystyki opisowe"
            }
        },
        "control_charts": {
            "control_charts": "Karty kontrolne ImR",
            "control_charts_desc": "Monitorowanie stabilności procesów za pomocą kart kontrolnych ImR. Karty kontrolne pozwalają na śledzenie zmian w procesach produkcyjnych lub badawczych, wykrywając ewentualne odchylenia od normy. Są niezbędnym narzędziem w zarządzaniu jakością i ciągłym doskonaleniu procesów.",
            "title": "Karty kontrolne ImR",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "data_format": "Plik powinien zawierać dwie kolumny: daty lub ID próbek oraz dane liczbowe.",
                "extra_columns": "Jeśli plik zawiera więcej niż 2 kolumny, dodatkowe kolumny zostaną pominięte.",
                "chart_info": "Generowane będą wykresy ImR, w tym wykres wartości indywidualnych (I) oraz ruchomego rozstępu (MR)."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd wczytanych danych",
                "data_preview": "Podgląd wczytanych danych (pierwsze 10 wierszy):",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej.",
                "error_two_columns": "Plik musi zawierać co najmniej 2 kolumny (Czas/ID, Wartość).",
                "warning_extra_columns": "Plik zawiera dodatkowe kolumny:",
                "select_result_column": "Wybierz kolumnę z wynikami do analizy:",
                "select_result_column_help": "Wybierz kolumnę zawierającą dane, które chcesz przeanalizować na karcie kontrolnej.",
                "using_first_two": "Wykorzystane zostaną tylko pierwsze dwie kolumny."
            },
            "chart_labels": {
                "time_series": "Czas/ID",
                "values": "Wartość",
                "individual_values": "I (Wartości indywidualne)",
                "moving_range": "MR (Ruchomy rozstęp)",
                "observation": "Obserwacja"
            },
            "analysis_results": {
                "normal_distribution_check": "Czy rozkład wartości I jest normalny (test α=0.05)?",
                "process_stable": "Czy proces jest stabilny wg reguł?",
                "show_I_chart": "Pokaż dane wykresu I (wartości indywidualne)",
                "show_MR_chart": "Pokaż dane wykresu MR (ruchomy rozstęp)",
                "I_chart_data": "Dane wykresu I (wartości indywidualne)",
                "MR_chart_data": "Dane wykresu MR (ruchomy rozstęp)"
            }
        },
        "process_capability": {
            "process_capability": "Analiza zdolności procesowej",
            "process_capability_desc": "Ocena zdolności procesu na podstawie wskaźników Cp i Cpk. Analiza zdolności procesowej pozwala ocenić, czy proces jest w stanie spełniać określone wymagania jakościowe. Wskaźniki Cp i Cpk pomagają w identyfikacji potencjalnych problemów i obszarów do poprawy.",
            "title": "Analiza zdolności procesowej",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane pomiarowe.",
                "set_spec_limits": "Ustaw dolną (LSL) i górną (USL) granicę specyfikacji oraz wartość docelową (Target).",
                "view_results": "Otrzymasz wykres analizy zdolności procesowej oraz wskaźniki Cp i Cpk."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "select_column": "Wybierz kolumnę do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "spec_settings": {
                "target": "Wartość docelowa (Target)",
                "lsl": "Dolna granica specyfikacji (LSL)",
                "usl": "Górna granica specyfikacji (USL)"
            },
            "plot": {
                "title": "Analiza zdolności procesowej",
                "x_label": "Wartości",
                "y_label": ""
            },
            "results": {
                "header": "Wyniki analizy",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Liczba próbek",
                "sample_mean": "Średnia próbki",
                "sample_std": "Odchylenie standardowe",
                "sample_max": "Maksimum",
                "sample_min": "Minimum",
                "sample_median": "Mediana",
                "pct_below_lsl": "Procent próbek poniżej LSL",
                "pct_above_usl": "Procent próbek powyżej USL"
            }
        },
        "stability_regression": {
            "stability_regression": "Regresja dla stabilności",
            "stability_regression_desc": "Analiza regresji dla danych stabilnościowych. Regresja stabilnościowa umożliwia przewidywanie trwałości produktów na podstawie wyników długoterminowych badań stabilności. Jest to kluczowe w przemyśle farmaceutycznym i spożywczym, gdzie stabilność produktów ma bezpośredni wpływ na ich bezpieczeństwo i skuteczność.",
            "title": "Analiza danych ze stabilności",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane stabilności.",
                "display_series": "Na wykresie zostaną wyświetlone wybrane serie wraz z liniami regresji.",
                "view_regression_results": "Pod wykresem znajdziesz tabelę z parametrami regresji dla wybranych serii."
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx lub xls):",
                "show_data_preview": "Pokaż podgląd danych",
                "data_preview": "Podgląd danych (pierwsze 12 wierszy):",
                "select_series": "Wybierz serie do analizy:",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "plot": {
                "data": "dane",
                "regression": "regresja",
                "spec_limit": "Limit specyfikacji",
                "x_label": "Czas (miesiące)",
                "title": "Analiza stabilności"
            },
            "regression_results": {
                "header": "Wyniki analizy regresji dla wybranych serii",
                "series": "Seria",
                "slope": "Nachylenie (slope)",
                "intercept": "Wyraz wolny (intercept)",
                "r_value": "Współczynnik korelacji (r)",
                "p_value": "Wartość p (p-value)",
                "std_err": "Odchylenie standardowe"
            }
        },
        "temp_humidity_analysis": {
            "temp_humidity": "Analiza temperatury i wilgotności",
            "temp_humidity_desc": "Analiza danych środowiskowych i identyfikacja przekroczeń limitów. Moduł ten pozwala na monitorowanie warunków środowiskowych, takich jak temperatura i wilgotność, oraz wykrywanie ewentualnych przekroczeń ustalonych limitów. Jest to szczególnie ważne w procesach produkcyjnych i magazynowych, gdzie warunki środowiskowe mogą wpływać na jakość i trwałość produktów.",
            "title": "Analiza temperatury i wilgotności",
            "instructions": {
                "header": "Instrukcje",
                "upload_file": "Wczytaj plik Excel zawierający dane temperatury i wilgotności.",
                "set_limits": "Ustaw limity temperatury i wilgotności za pomocą suwaków.",
                "view_results": "Przeglądaj wykresy oraz listę przekroczeń limitów."
            },
            "settings": {
                "temp_lower": "Dolna granica temperatury (\u00b0C)",
                "temp_upper": "Górna granica temperatury (\u00b0C)",
                "hum_lower": "Dolna granica wilgotności (%)",
                "hum_upper": "Górna granica wilgotności (%)"
            },
            "file_handling": {
                "choose_file": "Wybierz plik Excel (xlsx, xls):",
                "data_preview": "Podgląd danych (pierwsze 10 wierszy):",
                "error_processing_file": "Wystąpił błąd podczas analizy pliku",
                "no_file_uploaded": "Nie wybrano pliku - proszę wgrać plik Excel powyżej."
            },
            "statistics": {
                "temp_stats": "Statystyki temperatury",
                "hum_stats": "Statystyki wilgotności",
                "mean": "Średnia",
                "min": "Min",
                "max": "Max",
                "rsd": "Współczynnik zmienności (RSD %)"
            },
            "thresholds": {
                "crossings": "Przekroczenia limitów",
                "no_crossings": "Brak przekroczeń granic temperatury / wilgotności.",
                "time": "Czas",
                "temperature": "Temperatura",
                "humidity": "Wilgotność"
            },
            "plot": {
                "temp": "Temperatura",
                "hum": "Wilgotność",
                "temp_lower_limit": "Dolna granica temperatury",
                "temp_upper_limit": "Górna granica temperatury",
                "hum_lower_limit": "Dolna granica wilgotności",
                "hum_upper_limit": "Górna granica wilgotności",
                "x_label": "Czas",
                "y_label": "Wartość",
                "title": "Temperatura i Wilgotność"
            }
        },

    "pqr_module": {
        "title": "Moduł PQR",
        "instructions": {
            "header": "Instrukcje",
            "upload_file": "Prześlij plik z danymi",
            "select_series": "Wybierz serię do analizy",
            "input_spec_limits": "Wprowadź górny i dolny limit specyfikacji",
            "view_charts": "Wyświetl wykresy"
        },
        "file_handling": {
            "choose_file": "Wybierz plik",
            "error_two_columns": "Plik musi zawierać co najmniej dwie kolumny",
            "select_result_column": "Wybierz kolumnę z wynikami",
            "select_result_column_help": "Wybierz kolumnę zawierającą dane do analizy",
            "show_data_preview": "Pokaż podgląd danych",
            "data_preview": "Podgląd danych",
            "error_no_numeric_data": "Brak danych numerycznych do analizy",
            "error_processing_file": "Błąd podczas przetwarzania pliku",
            "no_file_uploaded": "Nie przesłano pliku"
        },
        "chart_labels": {
            "time_series": "Identyfikator serii",
            "values": "Wartości",
            "observation": "Obserwacja",
            "individual_values": "Wartości indywidualne",
            "moving_range": "Zakres ruchomy",
            "frequency": "Częstotliwość",
            "histogram_with_spec_limits": "Histogram z limitami specyfikacji",
            "control_chart_with_spec_limits": "Karta kontrolna z limitami specyfikacji"
        },
        "subheaders": {
            "imr_chart": "Karta kontrolna ImR",
            "cpk_analysis": "Analiza zdolności procesowej Cpk",
            "spec_limits_comparison": "Porównanie wyników z limitami specyfikacji"
        },
        "spec_limits": {
            "usl": "Górny limit specyfikacji (USL)",
            "lsl": "Dolny limit specyfikacji (LSL)"
        },
        "warnings": {
            "spec_limits_equal": "Górny i dolny limit specyfikacji są równe. Wprowadź poprawne wartości."
        },
        "cpk_results": {
            "mean": "Średnia",
            "std_dev": "Odchylenie standardowe",
            "cpk": "Wskaźnik Cpk"
        }
    }
    
    },
    "English": {
            "general": {
                "menu_title": "Menu",
                "intro": "Welcome to the Santo Pharmstat application!",
                "intro_desc": "The application allows for statistical and quality data analysis in a simple and intuitive way. In the side menu, you will find modules that help you analyze data from various perspectives.",
                "choose_page": "Choose a page:",
                "upload_data": "Upload data for analysis using the built-in forms.",
                "view_results": "The analysis results (charts, tables, statistics) will appear in the main area of the page.",
                "customize_view": "You can hide or display analysis details, adjusting the view to your needs.",
                "how_to_use": "How to use the application?"
            },
            "descriptive_statistics": {
                "descriptive_stats": "Descriptive Statistics",
                "descriptive_stats_desc": "Calculating basic statistics such as mean, median, and standard deviation. This module allows for quick and easy access to fundamental information about your data, which is crucial for further analysis. Descriptive statistics are the foundation of data analysis as they enable a quick understanding of data distribution and variability.",
                "title": "Descriptive Statistics",
                "instructions": {
                    "header": "Instructions",
                    "upload_file": "Upload an Excel file containing measurement data.",
                    "select_columns": "Select the columns for which you want to calculate descriptive statistics.",
                    "stats_summary": "You will receive a summary of the key statistics such as mean, median, standard deviation, and more.",
                    "normality_skew_kurtosis": "Additionally, assess the normality of the distribution and obtain information on skewness and kurtosis."
                },
                "file_handling": {
                    "choose_file": "Choose an Excel file (xlsx or xls):",
                    "show_data_preview": "Show data preview",
                    "data_preview": "Data preview (first 10 rows):",
                    "select_columns": "Select columns for analysis:",
                    "error_processing_file": "An error occurred while processing the file",
                    "no_file_uploaded": "No file selected - please upload an Excel file above."
                },
                "statistics": {
                    "shapiro_test": "Shapiro-Wilk p-value",
                    "skewness": "Skewness",
                    "kurtosis": "Kurtosis"
                }
            },
            "histogram_analysis": {
                "histograms": "Histograms",
                "histograms_desc": "Creating histograms with normality assessment and skewness and kurtosis analysis. This module allows you to visualize the distribution of your data and assess whether it exhibits characteristics of a normal distribution. Histograms are a useful tool for identifying the shape of data distribution and detecting any deviations or anomalies.",
                "title": "Histogram Analysis",
                "instructions": {
                    "header": "Instructions",
                    "upload_file": "Upload an Excel file containing measurement data.",
                    "select_column": "Select a column to analyze, generate a histogram, and display descriptive statistics.",
                    "normality_test": "Assess the normality of the distribution and obtain information on skewness and kurtosis."
                },
                "file_handling": {
                    "choose_file": "Choose an Excel file (xlsx or xls):",
                    "show_data_preview": "Show data preview",
                    "data_preview": "Data preview (first 10 rows):",
                    "select_column": "Select a column for analysis:",
                    "error_processing_file": "An error occurred while processing the file",
                    "no_file_uploaded": "No file selected - please upload an Excel file above."
                },
                "statistics": {
                    "sample_size": "Sample Size",
                    "mean": "Mean",
                    "std_dev": "Standard Deviation",
                    "max": "Maximum",
                    "min": "Minimum",
                    "median": "Median",
                    "rsd": "Relative Standard Deviation (RSD %)",
                    "shapiro_test": "Shapiro-Wilk Test",
                    "skewness": "Skewness",
                    "kurtosis": "Kurtosis"
                },
                "plot": {
                    "histogram_title": "Data Histogram",
                    "x_label": "Values",
                    "y_label": "Frequency"
                },
                "normality_results": {
                    "normal_distribution": "No reason to reject the hypothesis of normal distribution.",
                    "non_normal_distribution": "The data does not follow a normal distribution."
                }
            },
        "boxplot_charts": {
            "boxplot": "BoxPlot Charts",
            "boxplot_desc": "Visualizing data distribution and identifying outliers. BoxPlot charts provide a quick understanding of data distribution, showing the median, quartiles, and outliers. They are particularly useful for identifying potential measurement errors or unusual observations.",
            "title": "BoxPlot Charts",
            "instructions": {
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "select_columns": "Select columns for analysis to generate BoxPlot charts.",
                "view_stats": "You will receive descriptive statistics for the selected columns."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx, xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 5 rows):",
                "select_columns": "Select columns for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "title": "BoxPlot Charts for Selected Columns",
                "y_label": "Values"
            },
            "statistics": {
                "title": "Descriptive Statistics"
            }
        },
        "control_charts": {
            "control_charts": "ImR Control Charts",
            "control_charts_desc": "Monitoring process stability using ImR control charts. Control charts allow tracking of changes in production or research processes, detecting any deviations from the norm. They are an essential tool in quality management and continuous process improvement.",
            "title": "ImR Control Charts",
            "instructions": {
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "data_format": "The file should contain two columns: sample dates or IDs and numerical data.",
                "extra_columns": "If the file contains more than 2 columns, additional columns will be ignored.",
                "chart_info": "ImR charts will be generated, including the Individual Values (I) chart and the Moving Range (MR) chart."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above.",
                "error_two_columns": "The file must contain at least 2 columns (Time/ID, Value).",
                "warning_extra_columns": "The file contains extra columns:",
                "select_result_column": "Select the result column for analysis:",
                "select_result_column_help": "Choose the column containing the data you want to analyze in the control chart.",
                "using_first_two": "Only the first two columns will be used."
            },
            "chart_labels": {
                "time_series": "Time/ID",
                "values": "Value",
                "individual_values": "I (Individual Values)",
                "moving_range": "MR (Moving Range)",
                "observation": "Observation"
            },
            "analysis_results": {
                "normal_distribution_check": "Is the distribution of I values normal (α=0.05 test)?",
                "process_stable": "Is the process stable according to the rules?",
                "show_I_chart": "Show I Chart Data (Individual Values)",
                "show_MR_chart": "Show MR Chart Data (Moving Range)",
                "I_chart_data": "I Chart Data (Individual Values)",
                "MR_chart_data": "MR Chart Data (Moving Range)"
            }
        },
        "process_capability": {
            "process_capability": "Process Capability Analysis",
            "process_capability_desc": "Assessing process capability based on Cp and Cpk indices. Process capability analysis allows evaluating whether a process can meet specified quality requirements. Cp and Cpk indices help identify potential issues and areas for improvement.",
            "title": "Process Capability Analysis",
            "instructions": {
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing measurement data.",
                "set_spec_limits": "Set the lower (LSL) and upper (USL) specification limits and the target value.",
                "view_results": "You will receive a process capability analysis chart and Cp and Cpk indices."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 10 rows):",
                "select_column": "Select a column for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "spec_settings": {
                "target": "Target Value",
                "lsl": "Lower Specification Limit (LSL)",
                "usl": "Upper Specification Limit (USL)"
            },
            "plot": {
                "title": "Process Capability Analysis",
                "x_label": "Values",
                "y_label": ""
            },
            "results": {
                "header": "Analysis Results",
                "cp": "Cp",
                "cpk": "Cpk",
                "sample_size": "Sample Size",
                "sample_mean": "Sample Mean",
                "sample_std": "Standard Deviation",
                "sample_max": "Maximum",
                "sample_min": "Minimum",
                "sample_median": "Median",
                "pct_below_lsl": "Percentage of Samples Below LSL",
                "pct_above_usl": "Percentage of Samples Above USL"
            }
        },
        "stability_regression": {
            "stability_regression": "Stability Regression",
            "stability_regression_desc": "Regression analysis for stability data. Stability regression enables predicting product shelf life based on long-term stability study results. This is crucial in the pharmaceutical and food industries, where product stability directly impacts safety and efficacy.",
            "title": "Stability Data Analysis",
            "instructions": {
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing stability data.",
                "display_series": "The selected series will be displayed on the chart along with regression lines.",
                "view_regression_results": "Below the chart, you will find a table with regression parameters for the selected series."
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx or xls):",
                "show_data_preview": "Show data preview",
                "data_preview": "Data preview (first 12 rows):",
                "select_series": "Select series for analysis:",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "plot": {
                "data": "data",
                "regression": "regression",
                "spec_limit": "Specification Limit",
                "x_label": "Time (months)",
                "title": "Stability Analysis"
            },
            "regression_results": {
                "header": "Regression Analysis Results for Selected Series",
                "series": "Series",
                "slope": "Slope",
                "intercept": "Intercept",
                "r_value": "Correlation Coefficient (r)",
                "p_value": "p-value",
                "std_err": "Standard Error"
            }
        },
        "temp_humidity_analysis": {
            "temp_humidity": "Temperature and Humidity Analysis",
            "temp_humidity_desc": "Environmental data analysis and identification of limit exceedances. This module allows monitoring environmental conditions, such as temperature and humidity, and detecting any exceedances of established limits. It is particularly important in production and storage processes where environmental conditions can affect product quality and durability.",
            "title": "Temperature and Humidity Analysis",
            "instructions": {
                "header": "Instructions",
                "upload_file": "Upload an Excel file containing temperature and humidity data.",
                "set_limits": "Set temperature and humidity limits using sliders.",
                "view_results": "Browse charts and the list of limit exceedances."
            },
            "settings": {
                "temp_lower": "Lower Temperature Limit (°C)",
                "temp_upper": "Upper Temperature Limit (°C)",
                "hum_lower": "Lower Humidity Limit (%)",
                "hum_upper": "Upper Humidity Limit (%)"
            },
            "file_handling": {
                "choose_file": "Choose an Excel file (xlsx, xls):",
                "data_preview": "Data preview (first 10 rows):",
                "error_processing_file": "An error occurred while processing the file",
                "no_file_uploaded": "No file selected - please upload an Excel file above."
            },
            "statistics": {
                "temp_stats": "Temperature Statistics",
                "hum_stats": "Humidity Statistics",
                "mean": "Mean",
                "min": "Minimum",
                "max": "Maximum",
                "rsd": "Relative Standard Deviation (RSD %)"
            },
            "thresholds": {
                "crossings": "Limit Exceedances",
                "no_crossings": "No temperature/humidity limit exceedances.",
                "time": "Time",
                "temperature": "Temperature",
                "humidity": "Humidity"
            },
            "plot": {
                "temp": "Temperature",
                "hum": "Humidity",
                "temp_lower_limit": "Lower Temperature Limit",
                "temp_upper_limit": "Upper Temperature Limit",
                "hum_lower_limit": "Lower Humidity Limit",
                "hum_upper_limit": "Upper Humidity Limit",
                "x_label": "Time",
                "y_label": "Value",
                "title": "Temperature and Humidity"
            }
        },

    "pqr_module": {
        "title": "PQR Module",
        "instructions": {
            "header": "Instructions",
            "upload_file": "Upload data file",
            "select_series": "Select series for analysis",
            "input_spec_limits": "Enter upper and lower specification limits",
            "view_charts": "View charts"
        },
        "file_handling": {
            "choose_file": "Choose file",
            "error_two_columns": "The file must contain at least two columns",
            "select_result_column": "Select result column",
            "select_result_column_help": "Choose the column containing data for analysis",
            "show_data_preview": "Show data preview",
            "data_preview": "Data preview",
            "error_no_numeric_data": "No numeric data available for analysis",
            "error_processing_file": "Error processing file",
            "no_file_uploaded": "No file uploaded"
        },
        "chart_labels": {
            "time_series": "Series Identifier",
            "values": "Values",
            "observation": "Observation",
            "individual_values": "Individual Values",
            "moving_range": "Moving Range",
            "frequency": "Frequency",
            "histogram_with_spec_limits": "Histogram with Specification Limits",
            "control_chart_with_spec_limits": "Control Chart with Specification Limits"
        },
        "subheaders": {
            "imr_chart": "ImR Control Chart",
            "cpk_analysis": "Process Capability Analysis Cpk",
            "spec_limits_comparison": "Comparison of Results with Specification Limits"
        },
        "spec_limits": {
            "usl": "Upper Specification Limit (USL)",
            "lsl": "Lower Specification Limit (LSL)"
        },
        "warnings": {
            "spec_limits_equal": "Upper and lower specification limits are equal. Please enter valid values."
        },
        "cpk_results": {
            "mean": "Mean",
            "std_dev": "Standard Deviation",
            "cpk": "Cpk Index"
        }
    }
        
        },
        "Русский": {
            "general": {
                "menu_title": "Меню",
                "intro": "Добро пожаловать в приложение Santo Pharmstat!",
                "intro_desc": "Приложение позволяет просто и интуитивно проводить анализ статистических и качественных данных. В боковом меню вы найдёте модули, которые помогут вам анализировать данные с различных позиций.",
                "choose_page": "Выберите страницу:",
                "upload_data": "Загрузите данные для анализа с помощью встроенных форм.",
                "view_results": "Результаты анализа (графики, таблицы, статистика) появятся в главной области страницы.",
                "customize_view": "Вы можете скрывать или отображать детали анализа, настраивая вид согласно вашим потребностям.",
                "how_to_use": "Как использовать приложение?"
            },
            "descriptive_statistics": {
                "descriptive_stats": "Описательная статистика",
                "descriptive_stats_desc": "Вычисление основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение. Этот модуль позволяет быстро и легко получить основную информацию о ваших данных, что является ключевым для дальнейшего анализа. Описательная статистика является основой анализа данных, так как позволяет быстро понять распределение и изменчивость данных.",
                "title": "Описательная статистика",
                "instructions": {
                    "header": "Инструкции",
                    "upload_file": "Загрузите файл Excel с данными измерений.",
                    "select_columns": "Выберите столбцы для расчета описательной статистики.",
                    "stats_summary": "Вы получите сводку основных статистических показателей, таких как среднее значение, медиана, стандартное отклонение и другие.",
                    "normality_skew_kurtosis": "Дополнительно вы сможете оценить нормальность распределения и получить информацию о асимметрии и эксцессе."
                },
                "file_handling": {
                    "choose_file": "Выберите файл Excel (xlsx или xls):",
                    "show_data_preview": "Показать предварительный просмотр загруженных данных",
                    "data_preview": "Предварительный просмотр загруженных данных (первые 10 строк):",
                    "select_columns": "Выберите столбцы для анализа:",
                    "error_processing_file": "Произошла ошибка при анализе файла",
                    "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
                },
                "statistics": {
                    "shapiro_test": "Шапиро-Уилка p-значение",
                    "skewness": "Асимметрия",
                    "kurtosis": "Эксцесс"
                }
            },
            "histogram_analysis": {
                "histograms": "Гистограммы",
                "histograms_desc": "Создание гистограмм с оценкой нормальности распределения и анализом асимметрии и эксцесса. Этот модуль позволяет визуализировать распределение ваших данных и оценить, имеют ли они характеристики нормального распределения. Гистограммы являются полезным инструментом для идентификации формы распределения данных и выявления любых отклонений или аномалий.",
                "title": "Анализ гистограмм",
                "instructions": {
                    "header": "Инструкции",
                    "upload_file": "Загрузите файл Excel с данными измерений.",
                    "select_column": "Выберите столбец для анализа, чтобы создать гистограмму и отобразить описательную статистику.",
                    "normality_test": "Оцените нормальность распределения и получите информацию о асимметрии и эксцессе."
                },
                "file_handling": {
                    "choose_file": "Выберите файл Excel (xlsx или xls):",
                    "show_data_preview": "Показать предварительный просмотр данных",
                    "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                    "select_column": "Выберите столбец для анализа:",
                    "error_processing_file": "Произошла ошибка при анализе файла",
                    "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
                },
                "statistics": {
                    "sample_size": "Количество образцов",
                    "mean": "Среднее значение",
                    "std_dev": "Стандартное отклонение",
                    "max": "Максимум",
                    "min": "Минимум",
                    "median": "Медиана",
                    "rsd": "Коэффициент вариации (RSD %)",
                    "shapiro_test": "Тест Шапиро-Уилка",
                    "skewness": "Асимметрия",
                    "kurtosis": "Эксцесс"
                },
                "plot": {
                    "histogram_title": "Гистограмма данных",
                    "x_label": "Значения",
                    "y_label": "Частота"
                },
                "normality_results": {
                    "normal_distribution": "Нет оснований для отклонения гипотезы о нормальности распределения.",
                    "non_normal_distribution": "Данные не соответствуют нормальному распределению."
                }
            },
            "boxplot_charts": {
                "boxplot": "Ящичные диаграммы (BoxPlot)",
                "boxplot_desc": "Визуализация распределения данных и идентификация выбросов. Ящичные диаграммы обеспечивают быстрое понимание распределения данных, показывая медиану, квартили и выбросы. Они особенно полезны для выявления потенциальных ошибок измерения или необычных наблюдений.",
                "title": "Ящичные диаграммы (BoxPlot)",
                "instructions": {
                    "header": "Инструкции",
                    "upload_file": "Загрузите файл Excel с данными измерений.",
                    "select_columns": "Выберите столбцы для анализа, чтобы создать ящичные диаграммы.",
                    "view_stats": "Вы получите описательную статистику для выбранных столбцов."
                },
                "file_handling": {
                    "choose_file": "Выберите файл Excel (xlsx, xls):",
                    "show_data_preview": "Показать предварительный просмотр данных",
                    "data_preview": "Предварительный просмотр данных (первые 5 строк):",
                    "select_columns": "Выберите столбцы для анализа:",
                    "error_processing_file": "Произошла ошибка при анализе файла",
                    "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel выше."
                },
                "plot": {
                    "title": "Ящичные диаграммы для выбранных столбцов",
                    "y_label": "Значения"
                },
                "statistics": {
                    "title": "Описательная статистика"
                }
            },
            "control_charts": {
                "control_charts": "Контрольные карты ImR",
                "control_charts_desc": "Мониторинг стабильности процессов с использованием контрольных карт ImR. Контрольные карты позволяют отслеживать изменения в производственных или исследовательских процессах, выявляя любые отклонения от нормы. Они являются неотъемлемым инструментом в управлении качеством и непрерывном улучшении процессов.",
                "title": "Контрольные карты ImR",
                "instructions": {
                    "header": "Инструкции",
                    "upload_file": "Загрузите файл Excel с измерительными данными.",
                    "data_format": "Файл должен содержать два столбца: даты или идентификаторы образцов и численные данные.",
                    "extra_columns": "Если файл содержит более двух столбцов, дополнительные столбцы будут проигнорированы.",
                    "chart_info": "Будут сгенерированы графики ImR, включая график индивидуальных значений (I) и скользящего диапазона (MR)."
                },
                "file_handling": {
                    "choose_file": "Выберите файл Excel (xlsx или xls):",
                    "show_data_preview": "Показать предварительный просмотр данных",
                    "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                    "error_processing_file": "Ошибка при обработке файла",
                    "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel.",
                    "error_two_columns": "Файл должен содержать как минимум 2 столбца (Время/ID, Значение).",
                    "warning_extra_columns": "Файл содержит дополнительные столбцы:",
                    "select_result_column": "Выберите столбец с результатами для анализа:",
                    "select_result_column_help": "Выберите столбец, содержащий данные, которые вы хотите проанализировать на контрольной карте.",
                    "using_first_two": "Будут использованы только первые два столбца."
                },
                "chart_labels": {
                    "time_series": "Время/ID",
                    "values": "Значение",
                    "individual_values": "I (Индивидуальные значения)",
                    "moving_range": "MR (Скользящий диапазон)",
                    "observation": "Наблюдение"
                },
                "analysis_results": {
                    "normal_distribution_check": "Распределение значений I является нормальным (тест α=0.05)?",
                    "process_stable": "Процесс стабилен в соответствии с правилами?",
                    "show_I_chart": "Показать данные графика I (индивидуальные значения)",
                    "show_MR_chart": "Показать данные графика MR (скользящий диапазон)",
                    "I_chart_data": "Данные графика I (индивидуальные значения)",
                    "MR_chart_data": "Данные графика MR (скользящий диапазон)"
                }
            },
            "process_capability": {
                "process_capability": "Анализ способности процесса",
                "process_capability_desc": "Оценка способности процесса на основе показателей Cp и Cpk. Анализ способности процесса позволяет оценить, может ли процесс удовлетворять определенным требованиям качества. Показатели Cp и Cpk помогают выявить потенциальные проблемы и области для улучшения.",
                "title": "Анализ способности процесса",
                "instructions": {
                    "header": "Инструкции",
                    "upload_file": "Загрузите файл Excel с измерительными данными.",
                    "set_spec_limits": "Установите нижний (LSL) и верхний (USL) пределы спецификации и целевое значение (Target).",
                    "view_results": "Вы получите график анализа способности процесса и показатели Cp и Cpk."
                },
                "file_handling": {
                    "choose_file": "Выберите файл Excel (xlsx или xls):",
                    "show_data_preview": "Показать предварительный просмотр данных",
                    "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                    "select_column": "Выберите столбец для анализа:",
                    "error_processing_file": "Ошибка при обработке файла",
                    "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel."
                },
                "spec_settings": {
                    "target": "Целевое значение (Target)",
                    "lsl": "Нижний предел спецификации (LSL)",
                    "usl": "Верхний предел спецификации (USL)"
                },
                "plot": {
                    "title": "Анализ способности процесса",
                    "x_label": "Значения",
                    "y_label": ""
                },
                "results": {
                    "header": "Результаты анализа",
                    "cp": "Cp",
                    "cpk": "Cpk",
                    "sample_size": "Количество образцов",
                    "sample_mean": "Среднее значение образцов",
                    "sample_std": "Стандартное отклонение",
                    "sample_max": "Максимум",
                    "sample_min": "Минимум",
                    "sample_median": "Медиана",
                    "pct_below_lsl": "Процент образцов ниже LSL",
                    "pct_above_usl": "Процент образцов выше USL"
                }
            },
            "stability_regression": {
                        "stability_regression": "Регрессия для стабильности",
                        "stability_regression_desc": "Анализ регрессии для данных стабильности. Регрессия стабильности позволяет прогнозировать срок годности продуктов на основе долгосрочных исследований стабильности. Это особенно важно в фармацевтической и пищевой промышленности, где стабильность продуктов напрямую влияет на их безопасность и эффективность.",
                        "title": "Анализ данных стабильности",
                        "instructions": {
                            "header": "Инструкции",
                            "upload_file": "Загрузите файл Excel с данными стабильности.",
                            "display_series": "На графике будут отображены выбранные серии с линиями регрессии.",
                            "view_regression_results": "Под графиком вы найдете таблицу с параметрами регрессии для выбранных серий."
                        },
                        "file_handling": {
                            "choose_file": "Выберите файл Excel (xlsx или xls):",
                            "show_data_preview": "Показать предварительный просмотр данных",
                            "data_preview": "Предварительный просмотр данных (первые 12 строк):",
                            "select_series": "Выберите серии для анализа:",
                            "error_processing_file": "Произошла ошибка при анализе файла",
                            "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel."
                        },
                        "plot": {
                            "data": "данные",
                            "regression": "регрессия",
                            "spec_limit": "Предел спецификации",
                            "x_label": "Время (месяцы)",
                            "title": "Анализ стабильности"
                        },
                        "regression_results": {
                            "header": "Результаты анализа регрессии для выбранных серий",
                            "series": "Серия",
                            "slope": "Наклон (slope)",
                            "intercept": "Перехват (intercept)",
                            "r_value": "Коэффициент корреляции (r)",
                            "p_value": "P-значение (p-value)",
                            "std_err": "Стандартная ошибка"
                        }
                    },
                    "temp_humidity_analysis": {
                        "temp_humidity": "Анализ температуры и влажности",
                        "temp_humidity_desc": "Анализ данных окружающей среды и идентификация превышений лимитов. Этот модуль позволяет мониторить условия окружающей среды, такие как температура и влажность, и выявлять любые превышения установленных лимитов. Это особенно важно в производственных и складских процессах, где условия окружающей среды могут влиять на качество и долговечность продуктов.",
                        "title": "Анализ температуры и влажности",
                        "instructions": {
                            "header": "Инструкции",
                            "upload_file": "Загрузите файл Excel с данными температуры и влажности.",
                            "set_limits": "Установите лимиты температуры и влажности с помощью ползунков.",
                            "view_results": "Просматривайте графики и список превышений лимитов."
                        },
                        "settings": {
                            "temp_lower": "Нижний предел температуры (°C)",
                            "temp_upper": "Верхний предел температуры (°C)",
                            "hum_lower": "Нижний предел влажности (%)",
                            "hum_upper": "Верхний предел влажности (%)"
                        },
                        "file_handling": {
                            "choose_file": "Выберите файл Excel (xlsx, xls):",
                            "data_preview": "Предварительный просмотр данных (первые 10 строк):",
                            "error_processing_file": "Произошла ошибка при анализе файла",
                            "no_file_uploaded": "Файл не выбран - пожалуйста, загрузите файл Excel."
                        },
                        "statistics": {
                            "temp_stats": "Статистика температуры",
                            "hum_stats": "Статистика влажности",
                            "mean": "Среднее",
                            "min": "Минимум",
                            "max": "Максимум",
                            "rsd": "Коэффициент вариации (RSD %)"
                        },
                        "thresholds": {
                            "crossings": "Превышения лимитов",
                            "no_crossings": "Превышений температурных/влажностных лимитов не обнаружено.",
                            "time": "Время",
                            "temperature": "Температура",
                            "humidity": "Влажность"
                        },
                        "plot": {
                            "temp": "Температура",
                            "hum": "Влажность",
                            "temp_lower_limit": "Нижний предел температуры",
                            "temp_upper_limit": "Верхний предел температуры",
                            "hum_lower_limit": "Нижний предел влажности",
                            "hum_upper_limit": "Верхний предел влажности",
                            "x_label": "Время",
                            "y_label": "Значение",
                            "title": "Температура и Влажность"
                        }
                               
        },
    
            "pqr_module": {
        "title": "Модуль PQR",
        "instructions": {
            "header": "Инструкции",
            "upload_file": "Загрузите файл с данными",
            "select_series": "Выберите серию для анализа",
            "input_spec_limits": "Введите верхний и нижний пределы спецификации",
            "view_charts": "Просмотр графиков"
        },
        "file_handling": {
            "choose_file": "Выберите файл",
            "error_two_columns": "Файл должен содержать не менее двух столбцов",
            "select_result_column": "Выберите столбец с результатами",
            "select_result_column_help": "Выберите столбец, содержащий данные для анализа",
            "show_data_preview": "Показать предварительный просмотр данных",
            "data_preview": "Предварительный просмотр данных",
            "error_no_numeric_data": "Нет числовых данных для анализа",
            "error_processing_file": "Ошибка при обработке файла: {e}",
            "no_file_uploaded": "Файл не загружен"
        },
        "chart_labels": {
            "time_series": "Идентификатор серии",
            "values": "Значения",
            "observation": "Наблюдение",
            "individual_values": "Индивидуальные значения",
            "moving_range": "Скользящий диапазон",
            "frequency": "Частота",
            "histogram_with_spec_limits": "Гистограмма с пределами спецификации",
            "control_chart_with_spec_limits": "Контрольная карта с пределами спецификации"
        },
        "subheaders": {
            "imr_chart": "Контрольная карта ImR",
            "cpk_analysis": "Анализ способности процесса Cpk",
            "spec_limits_comparison": "Сравнение результатов с пределами спецификации"
        },
        "spec_limits": {
            "usl": "Верхний предел спецификации (USL)",
            "lsl": "Нижний предел спецификации (LSL)"
        },
        "warnings": {
            "spec_limits_equal": "Верхний и нижний пределы спецификации равны. Пожалуйста, введите корректные значения."
        },
        "cpk_results": {
            "mean": "Среднее",
            "std_dev": "Стандартное отклонение",
            "cpk": "Индекс Cpk"
        }
    }
        
        }
}
