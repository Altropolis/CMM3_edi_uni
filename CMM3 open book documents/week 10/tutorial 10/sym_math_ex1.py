import sympy as sym

# define some symbols
x = sym.Symbol('x')
y = sym.Symbol('y')
a = sym.Symbol('a')
c = sym.Symbol('c')
dydx = sym.Symbol('dydx')

# define the function y(x)
y=c*sym.sin(a*x)

# compute derivative
dydx = sym.diff(y, x)

# print them 
print('function y(x):     ',y)
print('derivative dy/dx:  ',dydx)
