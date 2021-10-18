data = set()
data_low = dict()
for i in range(int(input())):
    inp = input().split()
    for j in inp:
        data.add(j)
        data_low[j.lower()] = 0

for i in data_low:
    for j in data:
        if i == j.lower():
            data_low[j.lower()] += 1

for key, val in sorted(data_low.items(), key=lambda x: [-x[1], x[0]]):
    if val > 2:
        print(key, end='\n')
