import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

df = pd.read_parquet(path)

df['Hour'] = df['CMPLNT_FR_TM'].apply(lambda x: x.hour)
offense_times = df.groupby('Hour').size()

offense_times.index = offense_times.index.astype(str)
offense_times = offense_times.rename(index={
    0: 'Midnight',
    12: 'Noon'
})
offense_times = offense_times.rename(index = {
    '0': 'Midnight',
    '12': 'Noon'
})

plt.figure(figsize=(12, 6))
plt.title('Hours Offenses are Reported')
plt.suptitle('2006 - 2024')
plt.plot(offense_times.index, offense_times.values, marker= 'o')
plt.xticks(offense_times.index, rotation=45)
plt.xlabel('Hour of Day')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig(os.path.join(base_path, 'charts', 'crime_time_of_day.jpg')
plt.show()
