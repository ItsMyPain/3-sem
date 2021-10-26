person = {}
sers = {}
per = set()
s = []
for i in range(int(input())):
    inp = input().split()
    person[inp[0]] = inp[1]

for i in range(int(input())):
    inp = input().split()
    sers[inp[0]] = [inp[2], inp[3], inp[4]]

n = input()

for k, v in sers.items():
    if n in v:
        for i in v:
            per.add(i)

per.remove(n)

for i in per:
    s.append(person[i])

s.sort()
for i in s:
    print(i)
