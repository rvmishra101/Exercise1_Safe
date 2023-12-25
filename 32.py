import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('32.csv')
df['date'] = pd.to_datetime(df['week'] + '-1', format='%Y-%W-%w')
country_data = df[df['country'] == 'Israel']
x,y = country_data['date'][:len(country_data)-74], country_data['zscore'][:len(country_data)-74]

plt.figure(figsize=(8,5))
plt.plot(x,y, label='Z-score', color='blue')
plt.fill_between(x, -1, 2, color='green', alpha=0.1, label='Normal Range')
plt.axhline(y=0, color='grey', linestyle='--', label='Baseline')
plt.axhline(y=5, color='red', linestyle='--', label='Substantial Increase')
plt.axvspan(x.iloc[-4], x.iloc[-1], alpha=0.25, color='yellow',label='Adjusted Data')

plt.xlabel('Year')
plt.ylabel('Z-score')
plt.title('Z-score Trend Over Years for Israel')

plt.legend()
plt.grid(True)
# plt.savefig('32_created.png')
# plt.savefig('32_replicated.pdf')
plt.show()