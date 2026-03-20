import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

df = pd.read_parquet(path)

f_susp_m_vic = df[(df['Year'] >= 2006 )& (df['SUSP_SEX'] == 'F') & (df['VIC_SEX'] == 'M')]
offenses_f_susp_m_vic = f_susp_m_vic.groupby('OFNS_DESC').size()
offenses_f_susp_m_vic = offenses_f_susp_m_vic.sort_values(ascending=False)

offenses_f_susp_m_vic = offenses_f_susp_m_vic.rename(index = {
    'ASSAULT 3 & RELATED OFFENSES': 'ASSAULT 3',
    'OFF. AGNST PUB ORD SENSBLTY &': 'PUBLIC ORDER'
})

top_3 = offenses_f_susp_m_vic.iloc[:3]

plt.figure(figsize=(12, 6))
plt.title('Top 3 Offenses with Female suspect and Male Victim')
plt.suptitle('2006 - 2024')
plt.bar(top_3.index, top_3.values)
plt.xticks(top_3.index, rotation=45)
plt.xlabel('Offense Description')
plt.ylabel('Number of Crimes')
# loop through each crimes_per_borough.index value (i), top_10.values (v) and count crimes_per_boro.values
for i, v in enumerate(top_3.values):
    plt.text(i, v, v, ha='center')  #add text above bar, horizontal center

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig(os.path.join(base_path, 'charts', 'f_susp_m_vic_bar.jpg'))
plt.show()
