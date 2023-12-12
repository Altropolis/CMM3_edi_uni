import sympy as sym

y,x,w,TA,y0= sym.symbols('y x w TA y0')
y = TA/w * sym.cosh(w*x/TA) + y0 - (TA/w)
dy = sym.diff(y, x)
d2ydx2 = sym.diff(dy, x)
print(sym.simplify(d2ydx2))

d2ydx22 = w/TA * sym.sqrt(1+(dy)**2)
print(sym.simplify(d2ydx22))
'''
Part b)
    Been given values for y etc, asked to calcualte Ta
'''
import numpy as np
from scipy.optimize import fsolve

def y(Ta):
    x = 50
    y = 15
    y0 = 5
    w = 10
    return (Ta/w)*np.cosh((w/Ta)*x) + y0 - Ta/w - y

# Find the root (solution) for Ta
#Expect the tension to be relatively high
result = fsolve(y, 100)

print("Solution for Ta:", result)

def y_val(Ta):
    x = 50
    y = 15
    y0 = 5
    w = 10
    return (Ta/w)*np.cosh((w/Ta)*x) + y0 - Ta/w

if np.isclose(y_val(result), 15):
    y_Ta = y_val(result)
    print('The calculated Ta is correct, y is', y_Ta, 'when Ta is subbed in')
else:
    print('Ta is incorrect, try a new initial guess')