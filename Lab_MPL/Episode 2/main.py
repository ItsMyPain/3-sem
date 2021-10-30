import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

n = 0
m = 0
fig, axs = plt.subplots(3, 2, figsize=[12, 12])

with open("01.dat") as file:
    while True:
        line1 = file.readline()
        line2 = file.readline()
        if not line2: break
        x = [float(i) for i in line1.split()]
        y = [float(i) for i in line2.split()]
        axs[n, m].plot(x, y)
        axs[n, m].set_title('Frame %d' % (1 + n + 3 * m))
        axs[n, m].set_xlim([0, 16])
        axs[n, m].set_ylim([-12, 12])
        axs[n, m].grid()
        axs[n, m].xaxis.set_major_locator(ticker.MultipleLocator(1))
        axs[n, m].xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        axs[n, m].yaxis.set_major_locator(ticker.MultipleLocator(2))
        axs[n, m].yaxis.set_minor_locator(ticker.MultipleLocator(1))
        for label in (axs[n, m].get_xticklabels() + axs[n, m].get_yticklabels()):
            label.set_fontsize(8)
        if n == 2:
            n = 0
            m += 1
        else:
            n += 1
plt.subplots_adjust(wspace=0.3, hspace=0.4)
plt.savefig("res.png")
plt.show()
