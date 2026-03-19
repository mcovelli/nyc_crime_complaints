# nyc_crime_complaints_historic
Analysis of NYC Crime trends  

[Click Here to download dataset](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data)  
  
### Work in progress...  

- How to/installation guide
- Charts to README

## Summary  
An analysis of 9.4 million NYC crime complaints from 2006 through 2024 to examin overall crime trends, trends by borough, time, date and victim/suspect information using Python and Pandas to clean and Matplotlib to produce visuals, Ollama to generate an AI narrative and summary and Streamlit to create a dashboard.  
  
**Key findings:**  
  
• Brooklyn has the highest number of complaints, while State Island has the lowest.  
• Most crimes occur between noon and midnight.  
• Kidnapping has the highest reporting delay.  
• Harassment 2, Assault 3 & related offenses, and Offenses Against Public Order and Sensibility are top offenses with male suspects.  
• Crimes against women are disproportionately high across all boroughs.  
• Male suspects commit more than double as many crimes as female suspects.  
• The majority of crimes involve suspects between 24-44 years old.  
• Murder rates peak in Brooklyn in 2010, but have declined since 2021.  
• Petit Larceny is the most common reported offense across all boroughs.  
• Black suspects and victims account for an overwhelming majority of crime complaints.  
• The majority of suspect information remains missing.  
  
## Data Cleaning Log  
**Project:** NYPD Crime Complaints  
**Dataset:** NYPD Complaint Data Historic (NYC Open Date)  
**Tools:** Python/Pandas/Ollama/Streamlit  
**Date:** March 2026  
**Analyst:** Michael Covelli  

*unable to upload dataset to Github due to size limitations*  
[https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data)  
  
1. ### Dataset Overview  
   | Attribute  | Detail  |
   | ---------  | ------- |
   | Source | NYPD Complaint Data Historic (NYC Open Data) |
   | Original Format | CSV |
   | Exported Cleaned Format | parquet |
   | Total Rows | 9.44M |
   | Total Columns | 14 |
   | Date Range | 2006 - 2024 |
   
2. ### Data Dictionary  

   | # | Column  | Type  | Description |
   | --- | ---------  | ------- | -------- |
   | 1 | CMPLNT_NUM | text | Unique identifier for complaint records. |
   | 2 | CMPLNT_FR_DT | text | Exact date of occurence (if CMPLNT_TO_DT exists) |
   | 3 | CMPLNT_FR_TM | text | exact time of occurence (if CMPLNT_TO_TM exists) |
   | 4 | RPT_DT | text | Date the incident was reported to the police |
   | 5 | OFNS_DESC |	text | Description of offense corresponding with KY_CD  |
   | 6 | LAW_CAT_CD | text | Level of Offense (felony, misdemeanor, violation) |
   | 7 | BORO_NM | text | Name of the borough in which the incident occurred |
   | 8 | SUSP_AGE_GROUP | text | Suspect's Age Group |
   | 9 | SUSP_RACE | text | Suspect's Race Description |
   | 10 | SUSP_SEX | text | Suspect's Sex Desciption |
   | 11 | VIC_AGE_GROUP	| text | Victim's Age Group |	
   | 12 | VIC_RACE |	text | Victim's Race Desciption |
   | 13 | VIC_SEX |	text | Victim's Sex Description |
   | 14 | Year |	int | Derived from CMPLNT_FR_DT for filtering and time based analysis|  
  
   The original table contained 35 rows, 13 of which were chosen for this analysis. Columns like latitude, longitude, station_nm, etc. were too granular for a borough based analysis  
  
4. ### Number of Null values in each column  
  | Column | # of Nulls | Resolution |
  | ----- | ------ | ------ |
  | CMPLNT_FR_DT | 655 | dropped nulls |
  | CMPLNT_FR_TM | 48 | dropped nulls |
  | RPT_DT | 0 | n/a  |
  | OFNS_DESC | 18894 | dropped nulls |
  | LAW_CAT_CD | 0 |  n/a |
  | BORO_NM | 8719 | dropped nulls |
  | SUSP_AGE_GROUP | 4649568 | kept nulls, filtered out during analysis |
  | SUSP_RACE | 3753075 | kept nulls, filtered out during analysis |
  | SUSP_SEX | 3886446 | kept nulls, filtered out during analysis |
  | VIC_AGE_GROUP | 1623568 | kept, filtered out during analysis |
  | VIC_RACE | 760 | dropped  |
  | VIC_SEX | 308 | dropped |  
  
  *Approximately 40 - 49% of suspect information such as age, sex and race is missing which indicates the suspect wasn't found or no arrests had been made.  
  
5. ### Important Issues and Resolutions  
   | # | Issue  | Resolution  |
   | --- | ---------  | ------- |
   | 1 | Incorrect values for VIC_SEX ( D, E, L) | converted to null values |
   | 2 | Null values in several columns | dropped records with null dates, offense or borough |
   | 3 | values of '(null)' | removed str, converted to null values |
   | 4 | dates prior to the year 2006 may be incomplete or incorrect | filtered data prior 2006 for accuracy |
   | 5 | duplicate complaint numbers | kept most recent occurrence of duplicates |  
  
6. ### Data Type Corrections
   
   | Column | Original Type  | Corrected Type  |   Reason |
   | --- | ---------  | ------- | -------- |
   | CMPLNT_FR_DT | text | Date | Required for incident date analysis |
   | RPT_DT | text | date | Required for report delay analysis |
   | CMPLNT_FR_TM | text | time | Required for time based analysis |
   | Year | n/a | int | required for filtering and analysis |  
   
    
8. ### Data Verification Checks  
     
   7.1  
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
  
   7.2  
   **Question:** What is the date range of the dataset?
   **Risk:** Incorrect or imcomplete dates can indicate filtering errors or data quality issues 
    
   ``` {sql}
   print(df['CMPLNT_FR_DT'].min())
   print(df['CMPLNT_FR_DT'].max())
   ```    
    
   **Result:** 2006-01-01 to 2024-12-31

   7.3  
   **Question:** Are there any duplicate complaint numbers?  
   **Risk:** Duplicate complaint numbers can inflate crime counts across the analysis. Results could be skewed.  
    
   ``` {sql}
   print(df.duplicated(['CMPLNT_NUM']).sum())
   ```    
    
   **Result:** 1,105 duplicate complaint numbers dropped using drop_duplicates(), keeping the first occurrence of each complaint number. Final cleaned dataset contains 9,441,720 unique complaints.
8. ### Notable Data Observations  
   | Observation | Detail | Action Taken |
   | --- | ---------  | ------- |
   | null values stored as '(null)' | null values are input as a string | Set '(null)' as NaN |
   | 40-49% suspect data is missing | Suggests low arrest rates or suspect wasn't found | records with null suspect data kept, filtered during analysis |
   | Years like 1010 and 111 | Suggests data integrity issues | filtered results from 2006 - 2024 |
   | Unexpected values in VIC_SEX | values D, E, and L | set these values to null |
   
9. ### Final Dataset Summary  
   | Metric | Value |
   | --- | ---------  |
   | Total Rows | 9.44M |
   | Date Range | 2006 - 2024 |
   | Validation Checks Passed | 3/3 |  
   
10. ### Known Limitations  
   - Years before 2006 may be inaccurate (e.g. 1010), trimmed down to 2006 - 2024
   - Analysis does not include precise location information such as longitude, latitude, station_nm.
   - Approximately 40 - 49% of suspect information such as age, sex and race is missing

*This code is MIT licensed*
