import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

df = pd.read_parquet(path)

df = df[(df['Year'] >= 2006)]
susp_age = df.groupby(['SUSP_SEX', 'VIC_SEX']).size()
susp_age = susp_age.sort_index(ascending=True)

susp_age_grouped = susp_age.unstack()
susp_age_grouped.plot(kind='bar')

plt.title('Comparison of Suspect and Victim\'s Genders')
plt.suptitle('2006 - 2024')
plt.xticks(rotation=45)
plt.xlabel('Suspect Gender')
ticks = plt.yticks()[0]
plt.yticks(ticks, [f'{int(v):,}' for v in ticks])
plt.legend(title = 'Victim Gender')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig(os.path.join(base_path, 'charts', 'susp_vic_sex.jpg'))
plt.show()
