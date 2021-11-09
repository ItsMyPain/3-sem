import numpy as np

a = np.loadtxt(input())
b = np.loadtxt(input())
x = np.fromstring(input(), sep=' ')

print(a @ a @ x @ b)
