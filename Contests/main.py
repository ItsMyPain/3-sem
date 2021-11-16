import pandas as pd

g_path = input()#'games001.csv'
r_path = input()#'rates001.csv'

games = pd.read_csv(g_path, sep=';')
rates = pd.read_csv(r_path, sep=';')

rates_mean = rates.groupby('id').mean()

data = games.merge(rates_mean, left_on='id', right_index=True)
res1 = data.sort_values(by='mark', ascending=False).head(3)[['name', 'mark']]

for v in res1.values:
    print(f'{v[0]} {v[1]:.3f}')

res2 = data[data['mark'] > 8.0].loc[:, ['company', 'mark']].groupby('company').count() \
    .sort_values(by='mark', ascending=False).head(1)
print(res2.index[0], res2.iloc[0].values[0])
