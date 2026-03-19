import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/mike/nyc-crime-ai/nyc_crime_clean.parquet'

df = pd.read_parquet(path)

m_susp_f_vic = df[(df['Year'] >= 2006 )& (df['SUSP_SEX'] == 'M') & (df['VIC_SEX'] == 'F')]
offenses_m_susp_f_vic = m_susp_f_vic.groupby('OFNS_DESC').size()
offenses_m_susp_f_vic = offenses_m_susp_f_vic.sort_values(ascending=False)

offenses_m_susp_f_vic = offenses_m_susp_f_vic.rename(index = {
    'ASSAULT 3 & RELATED OFFENSES': 'ASSAULT 3',
    'OFF. AGNST PUB ORD SENSBLTY &': 'PUBLIC ORDER'
})

top_3 = offenses_m_susp_f_vic.iloc[:3]

plt.figure(figsize=(12, 6))
plt.suptitle('2006 - 2024')
plt.title('Top 3 Offenses with Male suspect and Female Victim')
plt.bar(top_3.index, top_3.values)
plt.xticks(top_3.index, rotation=45)
plt.xlabel('Offense Description')
plt.ylabel('Number of Crimes')
# loop through each crimes_per_borough.index value (i), top_10.values (v) and count crimes_per_boro.values
for i, v in enumerate(top_3.values):
    plt.text(i, v, v, ha='center')  #add text above bar, horizontal center

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig('/Users/mike/nyc-crime-ai/m_susp_f_vic.jpg')
plt.show()