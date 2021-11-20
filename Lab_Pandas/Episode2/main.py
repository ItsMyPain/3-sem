import pandas as pd

Data = pd.read_csv('flights.csv', sep=',')
count = Data['CARGO'].value_counts()
print(count)
group = Data.groupby('CARGO')[['PRICE', 'WEIGHT']].sum()
print(group)
res = group.merge(count, left_index=True, right_index=True)
print(res)