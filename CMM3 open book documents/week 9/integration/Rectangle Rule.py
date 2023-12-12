# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:34:29 2020

@author: emc1977
"""
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt



def calculate_dx (a, b, n):
	return (b-a)/float(n)

def rect_rule (f, a, b, n):
	total = 0.0
	dx = calculate_dx(a, b, n)
	for k in range (0, n):
            total = total + f((a + (k*dx)))
	return dx*total

def f(x):
    return x**2 + 4*x - 12

r = rect_rule(f, -10, 10, 1000)


def error(f, a, b, k):
    q = quad(f, -10, 10)
    true_error = abs(k)-(q[0])
    return true_error

N_array = []

def N_inter(f, a, b, N):
    for i in range(1, N+1):
        r = rect_rule (f, a, b, i)
        N_array.append(r)
    return N_array

N = 100

plt.plot(range(1, N+1), N_inter(f, -10, 10, N))
        
print(rect_rule(f, -10, 10, 1000), error(f, -10, 10, r))