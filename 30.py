import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('30.csv')
df['date'] = pd.to_datetime(df['date'])
df = df[df['location'].isin(['Australia', 'India'])]
df = df[df['date'] <= '31-07-2022']
df['new_deaths_per_million_7day_avg'] = df.groupby('location')['new_deaths_per_million'].rolling(7).mean().reset_index(0, drop=True)

for location in ['Australia', 'India']:
    data = df[df['location'] == location]
    plt.plot(data['date'], data['new_deaths_per_million_7day_avg'], label=location)

plt.xlabel('Date')
plt.ylabel('New Confirmed COVID-19 Deaths Per Million People')
plt.title('7 day Rolling Average Graph')
plt.legend()
plt.grid(True)
# plt.savefig('30_created.png')
# plt.savefig('30_replicated.pdf')
plt.show()
