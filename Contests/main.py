a = list(int(i) for i in input().split())
a.sort(reverse=True)
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i])
        break
