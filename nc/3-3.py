from sympy import *
from sympy.plotting import plot

x = symbols('x')
f = 1.4**x - x - 3
fi = 1.4**x - 3

p1 = plot(f, show=False)
p1.append(plot(fi, show=False)[0])
p1.show()
