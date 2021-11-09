import numpy as np

N, M = map(int, input().split())
K = int(input())
st = np.ones(shape=(N, M))

for i in range(K):
    x, y, r = map(int, input().split())
    st[max(0, x - r):min(x + r + 1, N), max(0, y - r):min(y + r + 1, M)] = 0

print(int(st.sum()))