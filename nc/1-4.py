from sympy import symbols
from sympy import Matrix
from sympy import diff
from sympy import linsolve

x, y = symbols('x y')
f1 = x**2 + y**2 - 2.1
f2 = (x**2) / 2 - y**2 - 0.15269
eps = 0.01


def getVectorNorm(v):
    max = abs(v[0])
    for x in v:
        max = abs(x) if abs(x) > max else max
    return max


_J = Matrix([[diff(f1, x), diff(f1, y)], [diff(f2, x), diff(f2, y)]])


def J(x1, x2):
    return _J.subs([(x, x1), (y, x2)])


def F(x1, x2):
    return (Matrix)([f1.subs([(x, x1), (y, x2)]), f2.subs([(x, x1), (y, x2)])])


# Обычный метод Ньютона
count = 0
accuracy = eps + 1
x0 = [1, 1]
while accuracy > eps and count < 50:
    sigmaX = linsolve((J(x0[0], x0[1]), -F(x0[0], x0[1])))
    x1 = [sigmaX.args[0][0] + x0[0], sigmaX.args[0][1] + x0[1]]
    accuracy = getVectorNorm(sigmaX.args[0])
    x0 = x1
    count += 1

print(x0)

# Модифицированный метод Ньютона
count = 0
accuracy = eps + 1
x0 = [1, 1]
x00 = x0
while accuracy > eps and count < 50:
    sigmaX = linsolve((J(x00[0], x00[1]), -F(x0[0], x0[1])))
    x1 = [sigmaX.args[0][0] + x0[0], sigmaX.args[0][1] + x0[1]]
    accuracy = getVectorNorm([x1[0] - x0[0], x1[1] - x0[1]])
    x0 = x1
    count += 1

print(x0)

# Разностный метод Ньютона
h = 0.5


def A(x1, x2):
    return (Matrix)([[(f1.subs([(x, x1 + h), (y, x2)]) - f1.subs([(x, x1), (y, x2)])) / h, (f1.subs([(x, x1 + h), (y, x2)]) - f1.subs([(x, x1), (y, x2)])) / h],
                     [(f2.subs([(x, x1 + h), (y, x2)]) - f2.subs([(x, x1), (y, x2)])) / h, (f2.subs([(x, x1 + h), (y, x2)]) - f2.subs([(x, x1), (y, x2)])) / h]])


count = 0
accuracy = eps + 1
x0 = [1, 1]
while accuracy > eps and count < 50:
    sigmaX = linsolve((A(x0[0], x0[1]), -F(x0[0], x0[1])))
    x1 = [sigmaX.args[0][0] + x0[0], sigmaX.args[0][1] + x0[1]]
    accuracy = getVectorNorm([x1[0] - x0[0], x1[1] - x0[1]])
    x0 = x1
    count += 1

print(x0)
