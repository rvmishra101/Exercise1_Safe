import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('21.csv')
df = df[df['group']=='Total']
for year in [2020,2021,2022,2017,2018,2019]:
    plt.plot('week', 'value', data=df[df['year'] == year], label=year)
plt.plot(list(range(53)), [0]*53, label='baseline',linestyle='dashed')
plt.xlabel('Week')
plt.ylabel('Excess Deaths')
plt.title('Excess Deaths in Europe')
plt.legend()
# plt.savefig('21_created.png')
# plt.savefig('21_replicated.pdf')
plt.show()