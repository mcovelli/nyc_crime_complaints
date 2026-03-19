import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/mike/nyc-crime-ai/nyc_crime_clean.parquet'

df = pd.read_parquet(path)

df['reporting_delay'] = df['RPT_DT'] - df['CMPLNT_FR_DT']
df['reporting_delay'] = df['reporting_delay'].dt.days
df = df[df['reporting_delay'] >= 0]
reporting_delay = df.groupby('OFNS_DESC')['reporting_delay'].median()
reporting_delay = reporting_delay.sort_values(ascending=False)

reporting_delay = reporting_delay.rename(index= {
    'KIDNAPPING AND RELATED OFFENSES': 'KIDNAPPING',
    'ABORTION': 'ILLEGAL ABORTION',
    'OFFENSES AGAINST MARRIAGE UNCL': 'MARRIAGE OFFENSES'
})

top_5 = reporting_delay.iloc[:5]

print(top_5)

plt.figure(figsize=(12, 8))
plt.title('Top 5 Offenses with the highest reporting delay')
plt.suptitle('2006 - 2024')
plt.bar(top_5.index, top_5.values)
plt.xticks(top_5.index, rotation=45)
plt.xlabel('Offense')
plt.ylabel('Number of Days')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig('/Users/mike/nyc-crime-ai/report_delay.jpg')
plt.show()