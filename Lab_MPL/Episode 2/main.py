import matplotlib.pyplot as plt

num = 0
fig, axs = plt.subplots(nrows=1, ncols=6)

with open("01.dat") as file:
    while True:
        line1 = file.readline()
        line2 = file.readline()
        if not line2: break
        x = [float(i) for i in line1.split()]
        y = [float(i) for i in line2.split()]
        axs[num].plot(x, y)
        axs[num].set_title('Frame %d' % num)
        axs[num].set_xlim([0, 16])
        axs[num].set_ylim([-12, 12])
        num += 1

plt.savefig("res.png")
plt.show()
