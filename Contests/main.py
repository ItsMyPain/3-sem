import numpy as np

N, M = map(int, input().split())

st = np.zeros(shape=(N, M), dtype=np.int32)
for i in range(N):
    st[i:] = np.fromstring(input(), sep=' ')

print(st[st < -5].size)
print(- st[st < 0].sum())
print(st.max())
