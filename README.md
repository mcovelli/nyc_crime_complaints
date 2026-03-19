# nyc_crime_complaints_historic
Analysis of NYC Crime trends, Borough comparisons and offense types

### Work in progress...  

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
**Tool:** Python/Pandas/Ollama/Streamlit  
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
   | Total Columns | 13 |
   | Date Range | 2006 - 2024 |
   
2. ### Data Dictionary  

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

4. ### Number of Null values in each column
  | Column | # of Nulls | Resolution |
  | ----- | ------ | ------ |
  | CMPLNT_FR_DT | 655 | dropped nulls |
  | CMPLNT_FR_TM | 48 | dropped nulls |
  | RPT_DT | 0 | n/a  |
  | OFNS_DESC | 18894 | dropped nulls |
  | LAW_CAT_CD | 0 |  n/a |
  | BORO_NM | 8719 | dropped nulls |
  | SUSP_AGE_GROUP | 4649568 | kept nulls, filtered out during analysis  |
  | SUSP_RACE | 3753075 | kept nulls, filtered out during analysis |
  | SUSP_SEX | 3886446 | kept nulls, filtered out during analysis |
  | VIC_AGE_GROUP | 1623568 | kept, filtered out during analysis |
  | VIC_RACE | 760 | dropped  |
  | VIC_SEX | 308 | dropped |  

  *Approximately 40 - 49% of suspect information such as age, sex and race is missing which indicates the suspect wasn't found or no arrests had been made.  
  
6. ### Important Issues and Resolutions  
   | # | Issue  | Resolution  |
   | --- | ---------  | ------- |
   | 1 | Incorrect values for VIC_SEX ( D, E, L) | converted to null values |
   | 2 | Null values in several columns | dropped records with null dates, offense or borough |
   | 3 | values of '(null)' | removed str, converted to null values |
   | 4 | dates prior to the year 2006 may be incomplete or incorrect | filtered data prior 2006 for accuracy |  
  
8. ### Data Type Corrections
   
   | Column | Original Type  | Corrected Type  |   Reason |
   | --- | ---------  | ------- | -------- |
   | CMPLNT_FR_DT | text | Date | Required for incident date analysis |
   | RPT_DT | text | date | Required for report delay analysis |
   | CMPLNT_FR_TM | text | time | Required for time based analysis |
   
    
9. ### Data Verification Checks  
     
   5.1  
   **Question:**  
   **Risk:**  
    
   ``` {sql}

   ```    
    
   **Result:** 
   
  
10. ### Notable Data Observations  
   | Observation | Detail | Action Taken |
   | --- | ---------  | ------- |
   |   |   |   |  
     
11. ### Final Dataset Summary  
   | Metric | Value |
   | --- | ---------  |
   | Total Rows | 9.44M |
   | Date Range | 2006 - 2024 |
   | Validation Checks Passed |  |
   | Import Issues resolved |  |  
  
11. ### Known Limitations  
   - Years before 2006 may be inaccurate (e.g. 1010), trimmed down to 2006 - 2024
   - Analysis does not include precise location information such as longitude, latitude, station_nm.
   - Approximately 40 - 49% of suspect information such as age, sex and race is missing

*This code is MIT licensed*
