import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from PIL import Image

n = 0
m = 0
fig, axs = plt.subplots(3, 2, figsize=[12, 12])
fig1, axs1 = plt.subplots()

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
        axs[n, m].yaxis.set_major_locator(ticker.MultipleLocator(2))
        if n == 2:
            n = 0
            m += 1
        else:
            n += 1

        axs1.plot(x, y)
        axs1.set_title('Frame %d' % (1 + n + 3 * m))
        axs1.set_xlim([0, 16])
        axs1.set_ylim([-12, 12])
        axs1.grid()
        axs1.yaxis.set_major_locator(ticker.MultipleLocator(2))

        fig1.savefig(f'GIF/res{(1 + n + 3 * m)}.png')
        axs1.clear()

fig.subplots_adjust(wspace=0.3, hspace=0.4)
fig.savefig("res.png")
plt.close(fig)
# plt.show()
# ------------------------------------------------------ #


frames = []

for frame_number in range(1, 6):
    frame = Image.open(f'GIF/res{frame_number}.png')
    frames.append(frame)

frames.extend(frames[::-1])
frames.remove(frames[5])

frames[0].save('homer.gif', save_all=True, append_images=frames[1:], optimize=True, duration=400, loop=0)
