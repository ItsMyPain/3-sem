import matplotlib.pyplot as plt
from PIL import Image

for num in range(1, 6):
    fname = "../Data/00%d.dat" % num
    f = open(fname)
    n = int(f.readline())
    x = []
    y = []
    for i in range(n):
        r = f.readline().split()
        x.append(float(r[0]))
        y.append(float(r[1]))

    f.close()
    plt.plot(x, y, ".C%d" % num, label="00%d.dat" % num)
    plt.grid()
    plt.legend()
    plt.savefig("00%d.png" % num)
    plt.show()

# ---------------------------------------------------------------- #
frames = []

for frame_number in range(1, 6):
    frame = Image.open(f'00{frame_number}.png')
    frames.append(frame)

frames[0].save('homer.gif', save_all=True, append_images=frames[1:], optimize=True, duration=2000, loop=0)
