import sympy as sym

# define some symbols
x = sym.Symbol('x')
y = sym.Symbol('y')

a = sym.Symbol('a')
c = sym.Symbol('c')

z = sym.Symbol('z')
s = sym.Symbol('s')
s2 = sym.Symbol('s2')
s3 = sym.Symbol('s3')

dydx = sym.Symbol('dydx')
d2ydx2 = sym.Symbol('d2ydx2')

# define a function
y=c*sym.sin(a*x)

# compute derivatives
dydx = sym.diff(y, x)
d2ydx2 = sym.diff(dydx, x)


# define another function
z = dydx + d2ydx2
s = 1/y*dydx
s2 = sym.simplify(s)
s3 = sym.series(s2, x)


# print them 
print('----------------')
print(y)
print('----------------')
print(dydx)
print('----------------')
print(d2ydx2)
print('----------------')
print(z)
print('----------------')
print(s)
print('----------------')
print(s2)
print('----------------')
print(s3)
print('----------------')
