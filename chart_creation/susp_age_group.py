import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

df = pd.read_parquet(path)
df = df[(df['Year'] >= 2006) & (df['SUSP_AGE_GROUP'].isin(['<18', '18-24', '25-44', '45-64', '65+', 'UNKNOWN']))]
susp_age = df.groupby(['SUSP_SEX', 'SUSP_AGE_GROUP']).size()
susp_age = susp_age.sort_index(ascending=True)

susp_age_grouped = susp_age.unstack()

susp_age_grouped.T.plot(kind='bar')

plt.title('Number of Crimes in each age group by Gender')
plt.xticks(rotation=45)
plt.xlabel('Suspect Age Group')
ticks = plt.yticks()[0]
plt.yticks(ticks, [f'{int(v):,}' for v in ticks])
plt.legend(title = 'Suspect Gender')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig(os.path.join(base_path, 'charts', 'susp_age_group.jpg'))
plt.show()
