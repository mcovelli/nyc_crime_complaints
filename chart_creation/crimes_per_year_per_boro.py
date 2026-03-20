# Crimes per year across all boroughs

import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

# load cleaned dataset
df = pd.read_parquet(path)

crimes_per_year = df.groupby(['BORO_NM', 'Year']).size();

plt.figure(figsize=(12, 6))

# loop through df for each UNIQUE borough
for b in df['BORO_NM'].unique():
    plt.plot(crimes_per_year.loc[b].index, crimes_per_year.loc[b], marker= 'o', label= b) # x= index of b (current borough), y= b value
plt.title('Total Crimes Per Year Per Borough')

# Anchor legend to the top left above the chart
plt.legend(bbox_to_anchor=(0.075, 1.0), ncol=2)

# Years 2006 - 2024
plt.suptitle('2006 - 2024')

# x ticks = year
plt.xticks(crimes_per_year.loc[b].index, rotation=45)
plt.grid(True, alpha=.3)
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3) 
plt.savefig(os.path.join(base_path, 'charts', 'crimes_per_year_per_boro_plot.jpg'))
plt.show()
