# 🗽 NYC Crime Complaints Analysis

[![Live Dashboard](https://img.shields.io/badge/Streamlit-Live_Dashboard-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://nyccrimecomplaints.streamlit.app)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An analysis of **9.4 million** NYC crime complaints from 2006 through 2024, examining overall crime trends by borough, time of day, date, and victim/suspect demographics. Built with Python and Pandas for data cleaning, Matplotlib for visualizations, Ollama (Llama 3.2) for AI-generated narrative summaries, and Streamlit for an interactive dashboard.

---

## 🔗 Live Dashboard

**[nyccrimecomplaints.streamlit.app](https://nyccrimecomplaints.streamlit.app)**

---

## 📊 Key Findings

- **Brooklyn** has the highest number of complaints; **Staten Island** has the lowest
- Most crimes occur **between noon and midnight**
- **Kidnapping** has the highest reporting delay
- Harassment 2, Assault 3 & related offenses, and Offenses Against Public Order are the top offenses with male suspects
- Crimes against women are disproportionately high across all boroughs
- Male suspects commit more than **double** the crimes of female suspects
- The majority of crimes involve suspects aged **24–44**
- Murder rates peaked in Brooklyn in 2010 but have declined since 2021
- **Petit Larceny** is the most common reported offense across all boroughs
- Black suspects and victims account for a disproportionate share of crime complaints
- The majority of suspect information remains missing from reports

---

## 📈 Sample Charts

*More charts available in [`charts/`](https://github.com/mcovelli/nyc_crime_complaints/tree/main/charts)*

| Crime by Time of Day | Crimes Per Year by Borough |
|:---:|:---:|
| ![Time of Day](https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/crime_time_of_day.jpg?raw=true) | ![Per Year by Borough](https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/crimes_per_year_per_boro_plot.jpg?raw=true) |

| Crimes by Borough | Murder Rates |
|:---:|:---:|
| ![By Borough](https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/crimes_per_boro_bar.jpg?raw=true) | ![Murder Rates](https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/murder_rates_plot.jpg?raw=true) |

---

## 🗂️ Project Structure
