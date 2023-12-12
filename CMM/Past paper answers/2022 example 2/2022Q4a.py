# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:58:33 2023

@author: s2086913
"""


from sympy import symbols, diff, cos, exp, sqrt, Eq, solve, Function, init_printing
import math
import numpy as np

A0, b, m, t, w, k , phi  = symbols('A0 b m t w k phi')

x_function = Function('x')(t)

equation_42 = Eq(x_function, A0*exp(-b*t/2*m)*cos(w*t+phi))

dx_dt = diff(x_function, t)

d2x_dt2 = diff(dx_dt, t)

equation_41 = Eq(0,  m*d2x_dt2 + b*dx_dt + k*equation_42.rhs)

equation_41_simplified = equation_41.simplify()

solutions_for_A0 = solve(equation_41_simplified, A0)

if all(equation_41_simplified.subs(A0, sol).simplify() == True for sol in solutions_for_A0):
    print("Equation 1B is the general solution to Equation 1A.")
else:
    print("Equation 1B is not the general solution to Equation 1A.")