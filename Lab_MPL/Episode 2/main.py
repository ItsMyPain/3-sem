import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image

n = 0
m = 0
fig, axs = plt.subplots(3, 2, figsize=[12, 12])

with open("01.dat") as file:
    while True:
        line1 = file.readline()
        line2 = file.readline()
        if not line2:
            break
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
plt.close(fig)
# plt.show()
# ------------------------------------------------------ #


num = 0
with open("01.dat") as file:
    while True:
        fig, axs = plt.subplots()
        num += 1
        line1 = file.readline()
        line2 = file.readline()
        if not line2:
            break
        x = [float(i) for i in line1.split()]
        y = [float(i) for i in line2.split()]
        axs.plot(x, y)
        axs.set_title('Frame %d' % num)
        axs.set_xlim([0, 16])
        axs.set_ylim([-12, 12])
        axs.grid()
        axs.xaxis.set_major_locator(ticker.MultipleLocator(1))
        axs.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
        axs.yaxis.set_major_locator(ticker.MultipleLocator(2))
        axs.yaxis.set_minor_locator(ticker.MultipleLocator(1))

        plt.savefig(f'GIF/res{num}.png')
        plt.close(fig)

frames = []

for frame_number in range(1, 6):
    frame = Image.open(f'GIF/res{frame_number}.png')
    frames.append(frame)

frames.extend(frames[::-1])
frames.remove(frames[5])

frames[0].save('homer.gif', save_all=True, append_images=frames[1:], optimize=True, duration=400, loop=0)
