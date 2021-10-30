import matplotlib.pyplot as plt
import collections

w = 0.6
fig, ax = plt.subplots(2, 1, figsize=[14, 14])

st = collections.defaultdict(list)
dt = collections.defaultdict(list)

with open("01.txt") as file:
    for line in file:
        inp = line.split(';')
        t = inp[2].replace('\n', '')
        st[inp[0]].append(int(t))
        dt[inp[1]].append(int(t))

for key in st:
    a = [0] * 11
    for i in range(11):
        a[i] = st[key].count(i)
    st[key] = a

for key in dt:
    a = [0] * 11
    for i in range(11):
        a[i] = dt[key].count(i)
    dt[key] = a

for i in range(1, 11):
    nowst = [st[key][i] for key in st]
    oldst = [sum(st[key][j] for j in range(i)) for key in st]
    nowdt = [dt[key][i] for key in dt]
    olddt = [sum(dt[key][j] for j in range(i)) for key in dt]
    ax[0].bar(list(st.keys()), nowst, w, bottom=oldst, label='%d' % i)
    ax[1].bar(list(dt.keys()), nowdt, w, bottom=olddt, label='%d' % i)


ax[0].legend(loc='upper right', fontsize=9)
ax[1].legend(loc='upper right', fontsize=9)
plt.savefig("res.png")
plt.show()
