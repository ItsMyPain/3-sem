import pandas as pd
st = [[int(i) for i in input().split()] for i in range(int(input()))]
df = pd.DataFrame(st, columns=list('XYL'))
df1 = df[(df['L'] >= 10) & (df['X']**2 + df['Y']**2 <= 100)]
print(df1)
