import numpy as np
import sympy as sp
from sympy.plotting import plot


def f(x):
    return np.exp(1 - x) / np.cos(x**2)


a = 1
b = 2
n = 5
xs = np.sort(np.random.uniform(low=a, high=b, size=5))
ys = f(xs)
c = xs[0] + (b - a) / 10
print(xs, ys)


def getNewtonPolynomial(xs, ys):
    sum = 0
    x = sp.Symbol('x')
    for k in range(1, len(xs)):
        product = 1
        for j in range(0, k):
            product *= x - xs[j]
        sum += product * nDifFunc(xs, ys, 0, k - 1)
    return ys[0] + sum


def nDifFunc(xs, ys, i, k):
    if k == 0:
        if i == len(xs):
            return (ys[i] - ys[i - 1]) / (xs[i] - xs[i - 1])
        else:
            return (ys[i] - ys[i + 1]) / (xs[i] - xs[i + 1])

    return (nDifFunc(xs[i:len(xs) - 1], ys[i:len(xs) - 1], i, k - 1) - nDifFunc(xs[i + 1:len(xs)], ys[i + 1:len(xs)], i, k - 1)) / (xs[i] - xs[k + 1])


lp = getNewtonPolynomial([1.03644, 1.1408], [2.02386, 3.26417])
print(lp)
qp = sp.simplify(getNewtonPolynomial(
    [1.03644, 1.1408, 1.24228], [2.02386, 3.26417, 28.5067]))
p = sp.simplify(getNewtonPolynomial([1.03644, 1.1408, 1.24228, 1.39622, 1.52141], [
                2.02386, 3.26417, 28.5067, -1.82031, -0.876726]))
print(p)
print(qp)
p1 = plot(lp, show=False)
p2 = plot(qp, show=False)
p3 = plot(p, show=False)
p1.append(p2[0])
p1.append(p3[0])
p1.show()
