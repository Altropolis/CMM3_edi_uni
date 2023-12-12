# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:08:14 2020

@author: emc1977
"""

def naive_root(f, x_guess, tolerance, step_size):
 
    steps_taken = 0
 
    while abs(f(x_guess)) > tolerance:
        if f(x_guess) > 0:
            x_guess -= step_size
        elif f(x_guess) < 0:
            x_guess += step_size
        else:
            return x_guess
 
        steps_taken += 1
 
    return x_guess, steps_taken
 
f = lambda x: x**2 - 20
root, steps = naive_root(f, x_guess=4.5, tolerance=.01, step_size=.001)
print ("root is:", root)
print ("steps taken:", steps)
