a = list(i for i in input().split())
b = set()
for i in range(len(a)):
    try:
        f = open(a[i], 'r')
    except FileNotFoundError:
        f = open(a[i], 'w+')
    finally:
        b.update(set(f.read().split()))
print(*sorted(b))
