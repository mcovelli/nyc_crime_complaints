# Offense types per borough

import pandas as pd
import matplotlib.pyplot as plt

# path to data
path = '/Users/mike/nyc-crime-ai/nyc_crime_clean.parquet'

# load cleaned dataset
df = pd.read_parquet(path)

offense_by_boro = df.groupby(['BORO_NM', 'OFNS_DESC']).size();

offense_by_boro_grouped = offense_by_boro.unstack();
top_5_offenses = offense_by_boro_grouped.sum().sort_values(ascending=False).head(5).index
top_5_by_boro = offense_by_boro_grouped[top_5_offenses]

top_5_by_boro.plot(kind='bar', figsize=(12, 6))

plt.title('Offense Types by Borough')

# Anchor legend to the top left above the chart
plt.legend(bbox_to_anchor=(0.5, .65), ncol=2, labels = ['PETIT LARCENY', 'HARRASSMENT 2', 'ASSAULT 2', 'CRIMINAL MISCHIEF', 'GRAND LARCENY'])

# Years 2006 - 2024
plt.suptitle('2006 - 2024')

# x ticks = year
plt.xticks(rotation=45)
plt.grid(True, alpha=.3)
plt.xlabel('Borough')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig("/Users/mike/nyc-crime-ai/offense_by_boro.jpg")
plt.show()