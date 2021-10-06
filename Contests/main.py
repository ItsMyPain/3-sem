n = int(input())
massive = {}
for i in range(n):
    inp = input().split()
    massive[int(inp[0])] = int(inp[1])

print(massive)
smassive = sorted(massive.items(), key=lambda x: -x[1])

for i in smassive:
    print(i[0])
