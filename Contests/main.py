import numpy as np
import pandas as pd

try:
    N = int(input())
    data = pd.DataFrame(columns=['time', 'id', 'vit', 'ac', 'anti', 'neural', 'mch'])
    for i in range(N):
        data.loc[i] = [float(i) for i in input().split()]
    data = data[['id', 'neural']]
    count = data['id'].value_counts()
    d1 = pd.merge(data, count, left_on='id', right_index=True)
    d2 = d1[d1['id_y'] > 1]
    d4 = d2.groupby('id').apply(lambda x: x.max() - x.min())
    data4 = d4.sort_values(by='neural')
    if data4.empty:
        print(-1)
    else:
        a = []
        for i in data4.head(3).index:
            a.append(int(i))
        print(*sorted(a))
except:
    print(-1)
