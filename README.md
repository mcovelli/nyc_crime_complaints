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
| # | Column  | Type  | Description |
| --- | ---------  | ------- | -------- |
| 1 | CMPLNT_FR_DT | text | Exact date of occurence (if CMPLNT_TO_DT exists) |
| 2 | CMPLNT_FR_TM | text | exact time of occurence (if CMPLNT_TO_TM exists) |
| 3 | RPT_DT | text | Date the incident was reported to the police |
| 4 | OFNS_DESC |	text | Description of offense corresponding with KY_CD  |
| 5 | LAW_CAT_CD | text | Level of Offense (felony, misdemeanor, violation) |
| 6 | BORO_NM | text | Name of the borough in which the incident occurred |
| 7 | SUSP_AGE_GROUP | text | Suspect's Age Group |
| 8 | SUSP_RACE | text | Suspect's Race Description |
| 9 | SUSP_SEX | text | Suspect's Sex Desciption |
| 10 | VIC_AGE_GROUP	| text | Victim's Age Group |	
| 11 | VIC_RACE |	text | Victim's Race Desciption |
| 12 | VIC_SEX |	text | Victim's Sex Description |


  The original table contained 35 rows, 12 of which were chosen for this analysis. Columns like latitude, longitude, station_nm, etc. were too granular for a borough based analysis  
---
### Number of Null values in each column  
  | Column | # of Nulls | Resolution |
  | ----- | ------ | ------ |
  | CMPLNT_FR_DT | 655 | dropped nulls |
  | OFNS_DESC | 18894 | dropped nulls |
  | LAW_CAT_CD | 0 |  n/a |
  | BORO_NM | 8719 | dropped nulls |
  | SUSP_AGE_GROUP | 4649568 | kept nulls, filtered out during analysis  |
  | SUSP_AGE_GROUP | 4649568 | kept nulls, filtered out during analysis |
  | SUSP_RACE | 3753075 | kept nulls, filtered out during analysis |
  | SUSP_SEX | 3886446 | kept nulls, filtered out during analysis |
  | VIC_AGE_GROUP | 1623568 | kept, filtered out during analysis |
  | VIC_RACE | 760 | dropped  |
  | VIC_SEX | 308 | dropped |  

  
  *Approximately 40 - 49% of suspect information such as age, sex and race is missing which indicates the suspect wasn't found or no arrests had been made.  
---
### Important Issues and Resolutions  
   | # | Issue  | Resolution  |
   | --- | ---------  | ------- |
   | 1 | Incorrect values for VIC_SEX ( D, E, L) | converted to null values |
   | 2 | Null values in several columns | dropped records with null dates, offense or borough |
   | 3 | values of '(null)' | removed str, converted to null values |
   | 4 | dates prior to the year 2006 may be incomplete or incorrect | filtered data prior 2006 for accuracy |  
   | 4 | dates prior to the year 2006 may be incomplete or incorrect | filtered data prior 2006 for accuracy |
   | 5 | duplicate complaint numbers | kept most recent occurrence of duplicates |  
---
### Data Type Corrections

   | Column | Original Type  | Corrected Type  |   Reason |
   | --- | ---------  | ------- | -------- |
   | CMPLNT_FR_DT | text | Date | Required for incident date analysis |
   | RPT_DT | text | date | Required for report delay analysis |
   | CMPLNT_FR_TM | text | time | Required for time based analysis |
   | Year | n/a | int | required for filtering and analysis |  

---
### Data Verification Checks   
     
   **Question:**  
   **Risk:**  
   **Question:** How many rows were removed during the data cleaning process? 
   **Risk:** Removing too many rows indicate overly aggressive filter and data quality issues. Removing too few rows could suggest cleaning steps didn't execute properly.   
    
   ``` {sql}
   print(f'Rows after loading: {df.shape[0]:,}')
   print(f'Rows after dropping nulls: {df.shape[0]:,}')
   print(f'Rows after dropping duplicates: {df.shape[0]:,}')
   print(f'Rows after year filter: {df.shape[0]:,}')
   ```    
    
   **Result:**  
  Rows after loading: 9,491,946  
  Rows after dropping nulls: 9,463,661  
  Rows after dropping duplicates: 9,462,557  
  Rows after year filter: 9,441,720  
  Cleaned dataset: 9,441,720 rows, 14 columns
  
   **Question:** What is the date range of the dataset?
   **Risk:** Incorrect or imcomplete dates can indicate filtering errors or data quality issues 

   ``` {sql}
   print(df['CMPLNT_FR_DT'].min())
   print(df['CMPLNT_FR_DT'].max())
   ```    
    
   **Result:** 2006-01-01 to 2024-12-31

   **Question:** Are there any duplicate complaint numbers?  
   **Risk:** Duplicate complaint numbers can inflate crime counts across the analysis. Results could be skewed.  
    
   ``` {sql}
   print(df.duplicated(['CMPLNT_NUM']).sum())
   ```    

   **Result:** 1,105 duplicate complaint numbers dropped using drop_duplicates(), keeping the first occurrence of each complaint number. Final cleaned dataset contains 9,441,720 unique complaints.

---  
### Notable Data Observations  
   
   | Observation | Detail | Action Taken |
   | --- | ---------  | ------- |
   | 40-49% suspect data is missing | Suggests low arrest rates or suspect wasn't found | records with null suspect data kept, filtered during analysis |
   | Years like 1010 and 111 | Suggests data integrity issues | filtered results from 2006 - 2024 |
   | Unexpected values in VIC_SEX | values D, E, and L | set these values to null |  
   | null values stored as '(null)' | null values are input as a string | Set '(null)' as NaN |
---
### Final Dataset Summary  
   | Metric | Value |
   | --- | ---------  |
   | Total Rows | 9.44M |
   | Date Range | 2006 - 2024 |
   | Validation Checks Passed | 3/3 |
  
---
### Known Limitations  
   - Years before 2006 may be inaccurate (e.g. 1010), trimmed down to 2006 - 2024
   - Analysis does not include precise location information such as longitude, latitude, station_nm.
## 📄 License  
This project is licensed under the 
MIT License
.
