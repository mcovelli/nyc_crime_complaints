# Crimes per year across all boroughs

import pandas as pd
import matplotlib.pyplot as plt
import os

# path to data
base_path = os.path.dirname(__file__)
path = os.path.join(base_path, 'data', 'nyc_crime_clean.parquet')

# load cleaned dataset
df = pd.read_parquet(path)

crimes_per_year = df.groupby('Year').size();

plt.figure(figsize=(12, 6))
plt.plot(crimes_per_year.index, crimes_per_year.values, marker= 'o')
plt.title('Total Crimes Per Year')
plt.suptitle('2006 - 2024')
plt.xticks(crimes_per_year.index, rotation=45)
plt.grid(True, alpha=.3)
plt.xlabel('Year')
plt.ylabel('Number of Crimes')
plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig(os.path.join(base_path, 'charts', 'crimes_per_year_plot.jpg'))
plt.show()
