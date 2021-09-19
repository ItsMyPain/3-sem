a = list(i for i in input().split())
b = {a[i]: a.count(a[i]) for i in range(len(a))}
for x, y in sorted(b.items(), key=lambda x: [-x[1], x[0]]):
    print(y, x)
