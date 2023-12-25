import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('20.csv')
df['date'] = pd.to_datetime(df['Weekending'])
df['year'] = df['date'].dt.year
filtered_df = df[df['MMWRweek'] < 34]

year_deaths = filtered_df.groupby('year')['Deaths (weighted)'].sum().to_dict()
x,y = list(year_deaths.keys())[3:-1], list(year_deaths.values())[3:-1]
bars = plt.barh(x,y, color='blue' )

plt.xlabel('Deaths')
plt.ylabel('Years')
plt.gca().invert_yaxis()
plt.title('MORE Deaths in Ending Years')

for bar in bars:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
             f'{bar.get_width():,.0f}', va='center', ha='right', color='white', fontsize=8)

# plt.savefig('20_created.png')
# plt.savefig('20_replicated.pdf')
plt.show()