import numpy as np


def f(x):
    return np.log(2 + x) - 5 * x**3


eps = 10**-7
xs = np.arange(-1, 1, 0.1)
ys = f(xs)
print(np.arange(0.5, 0.6, 0.02), f(np.arange(0.5, 0.6, 0.02)))

a = 0.56
b = 0.58
for i in range(0, 101):
    c = (a + b) / 2
    fc = f(c)
    if f(a) * fc < 0:
        b = c
    elif fc != 0:
        a = c

    if abs(b - a) < eps or fc == 0:
        print('Решение х = ', c, ' получено на ', i, ' шаге.')
        break
