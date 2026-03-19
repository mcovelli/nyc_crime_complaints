import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/mike/nyc-crime-ai/nyc_crime_clean.parquet'

df = pd.read_parquet(path)

df = df[(df['Year'] >= 2006)]
susp_race = df.groupby(['SUSP_RACE', 'VIC_RACE']).size()

susp_race_grouped = susp_race.unstack()
susp_race_grouped = susp_race_grouped.rename(index= {
    'AMERICAN INDIAN/ALASKAN NATIVE': 'NATIVE AM.',
    'ASIAN / PACIFIC ISLANDER': 'ASIAN/PI',
    'BLACK HISPANIC': 'B. HISPANIC',
    'WHITE HISPANIC': 'W. HISPANIC'
})

susp_race_grouped.plot(kind='bar', figsize=(12, 8))
plt.title('Comparison of Suspect and Victim\'s Races')
plt.suptitle('2006 - 2024')
plt.xticks(rotation=45)
plt.xlabel('Suspect\'s Race')
ticks = plt.yticks()[0]
plt.yticks(ticks, [f'{int(v):,}' for v in ticks])
plt.legend(title = 'Victim\'s Race')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig('/Users/mike/nyc-crime-ai/susp_vic_race.jpg')
plt.show()
