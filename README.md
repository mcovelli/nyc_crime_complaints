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
|
 [Crime by Time of Day](https://github.com/mcovelli/nyc_crime_complaints/blob/main/charts/crime_time_of_day.jpg?raw=true)
|
 [Crimes Per Year by Borough](https://github.com/mcovelli/nyc_crime_complaints/blob/main/charts/crimes_per_year_per_boro_plot.jpg?raw=true)
|
[Time of Day](https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/crime_time_of_day.jpg?raw=true)
|
[
Per Year by Borough
](
https://github.com/mcovelli/nyc_crime_complaints/blob/e0f91506d72bb1cc592e3a8d73020d430b1e8c0f/charts/crimes_per_year_per_boro_plot.jpg?raw=true
)
|
 [Crimes by Borough](https://github.com/mcovelli/nyc_crime_complaints/blob/main/charts/crimes_per_boro_bar.jpg?raw=true) 
|
 [Murder Rates](https://github.com/mcovelli/nyc_crime_complaints/blob/main/charts/murder_rates_plot.jpg?raw=true)
|
---
## 🗂️ Project Structure

```text
nyc_crime_complaints/
├── app.py                   # Streamlit dashboard
├── nyc_crime_cleaning.py    # Data cleaning script
├── narrative.py             # AI narrative generation (Ollama)
├── narrative.md             # Generated narrative output
├── requirements.txt         # Python dependencies
├── chart_creation/          # Scripts for generating charts
├── charts/                  # Output chart images
└── data/                    # Dataset directory (not uploaded — see setup)
```  

## 🚀 Setup  
### Prerequisites  
Git  
Python 3.10+  
Ollama installed and running Llama 3.2:  

```
ollama pull llama3.2
ollama serve
```  
### Installation  
#### Clone the repository  

```
git clone https://github.com/mcovelli/nyc_crime_complaints.git
cd nyc_crime_complaints
```
#### Create and activate a virtual environment

```
python -m venv venv
```
# Mac/Linux
```
source venv/bin/activate
```  
# Windows  
```
venv\Scripts\activate
```  
#### Download the dataset  

Download NYPD Complaint Data Historic  
Save the file as NYPD_Complaint_Data_Historic.csv in the data/ directory 

#### Install dependencies  

```
pip install -r requirements.txt
```
#### Run the cleaning script
```
python nyc_crime_cleaning.py
```
#### Launch the dashboard
```
streamlit run app.py
```
Note: The dataset is too large to upload to GitHub (~1.5 GB). You must download it directly from NYC Open Data.

## 🧹 Data Cleaning Log  
| Attribute |	Detail |
|---------|-------------|
| Project	| NYPD Crime Complaints |
| Dataset |	NYPD Complaint Data Historic (NYC Open Data) |
| Tools	| Python · Pandas · Ollama · Streamlit |
| Date	| March 2026 |
| Analyst	| Michael Covelli |
---  
## 📄 License  
This project is licensed under the 
MIT License
.
