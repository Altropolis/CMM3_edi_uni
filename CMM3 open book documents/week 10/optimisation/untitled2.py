#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:45:42 2023

@author: alfie
"""

from sympy import Symbol, sin, diff, simplify, series

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
s = Symbol('s')
a = Symbol('a')
c = Symbol('c')
dydx = Symbol('dydx')
d2ydx2 = Symbol('d2ydx2')


y = c*sin(a*x)

dydx = diff(y, x)

d2ydx2 = diff(dydx, x)

z = dydx + d2ydx2

s = 1/y * dydx


#simplifies the function mathematically
t = simplify(s)

#find taylor series of s
k = simplify(series(t, x))

print('function y(x):          ', y)
print('derivative dy/dx:        ', dydx)
print('derivative d2y/dx2:        ', d2ydx2)
print('derivative z:        ', z)
print('derivative s:        ', s)
print('derivative s(simplified):        ', t)
print('derivative s(taylor series):        ', k)
