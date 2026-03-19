# Number of Crimes per Borough overall

import pandas as pd
import matplotlib.pyplot as plt

# path to data
path = '/Users/mike/nyc-crime-ai/nyc_crime_clean.parquet'

# load cleaned dataset
df = pd.read_parquet(path)

# Group by Borough Name
crimes_per_boro = df.groupby('BORO_NM').size();

# sort values (number of crimes) by descending
crimes_per_boro = crimes_per_boro.sort_values(ascending=False);

# create bar chart x = borough, y = number of crimes
plt.bar(crimes_per_boro.index, crimes_per_boro.values)

#title
plt.title('Total Crimes Per Borough')

#sub title indicating years
plt.suptitle('2006 - 2024')

# text for each tick (borough name)
plt.xticks(crimes_per_boro.index, rotation=45)

# label for x-axis
plt.xlabel('Borough')

# label for y-axis
plt.ylabel('Number of Crimes')

# y-axis
ticks = plt.yticks()[0]
plt.yticks(ticks, [f'{int(v):,}' for v in ticks])

# subtle drid lines on y-axis
plt.grid(axis='y', linestyle='-', alpha=.2)

# loop through each crimes_per_borough.index value (i), crimes_per_borough.values (v) and count crimes_per_boro.values
for i, v in enumerate(crimes_per_boro.values):
    plt.text(i, v, v, ha='center')  #add text above bar, horizontal center

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig("/Users/mike/nyc-crime-ai/crimes_per_boro_bar.jpg")
plt.show()