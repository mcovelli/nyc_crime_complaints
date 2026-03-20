import pandas as pd
import numpy as np
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'NYPD_Complaint_Data_Historic.csv')

# 13/35 columns loaded
cols_to_load = ['CMPLNT_NUM', 'CMPLNT_FR_DT', 'CMPLNT_FR_TM', 'RPT_DT', 'OFNS_DESC', 'LAW_CAT_CD', 'BORO_NM', 'SUSP_AGE_GROUP', 'SUSP_RACE', 'SUSP_SEX', 'VIC_AGE_GROUP', 'VIC_RACE', 'VIC_SEX']

# null values in dataset
na_values = ['(null)']

# load dataset, using columns, and set '(null)' as NaN
df = pd.read_csv(path, usecols=cols_to_load, low_memory=False, na_values=na_values)

#drop null rows with null values in specified columns
df = df.dropna(subset= ['CMPLNT_NUM', 'CMPLNT_FR_DT', 'OFNS_DESC', 'BORO_NM', 'CMPLNT_FR_TM'])

# Drop duplicate complaint numbers
df= df.drop_duplicates(subset=['CMPLNT_NUM'])

# convert column to datetime type
df['CMPLNT_FR_DT'] = pd.to_datetime(df['CMPLNT_FR_DT'], errors='coerce')
df['CMPLNT_FR_TM'] = pd.to_datetime(df['CMPLNT_FR_TM'], format='%H:%M:%S', errors='coerce')
df['CMPLNT_FR_TM'] = df['CMPLNT_FR_TM'].dt.time
df['RPT_DT'] = pd.to_datetime(df['RPT_DT'], errors='coerce')

# Replace invalid values in VIC_SEX with null
df['VIC_SEX'] = df['VIC_SEX'].replace({'D': np.nan, 'E': np.nan, 'L': np.nan})

# Filter out years before 2006
df['Year'] = df['CMPLNT_FR_DT'].dt.year
df = df[df['Year'] >= 2006]

# export clean dataframe to a new CSV
df.to_parquet(os.path.join(base_path, 'data', 'nyc_crime_clean.parquet'), index=False)

print(f'Cleaned dataset: {df.shape[0]:,} rows, {df.shape[1]} columns')
print(df.duplicated(['CMPLNT_NUM']).sum())
print('DONE!')

