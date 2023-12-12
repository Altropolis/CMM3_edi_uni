# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:57:24 2023

@author: s2086913
"""


from scipy.optimize import fsolve
import numpy as np

# Define the function representing the iterative equation
def equation(X, *args):
    return X - (1 / np.sin(args[0])) - 1/4

# Initial guess for the root
initial_guess = 2.0

# Use fsolve to find the root numerically
root, = fsolve(equation, initial_guess, args=(initial_guess,))

# Check if the root is within the specified domain (0 < X < 4)
if 0 < root < 4:
    print("Numerical root found:", root)
else:
    print("No root found within the specified domain.")
    
'''
The args parameter in the fsolve function allows you to pass additional parameters to the function you're 
trying to find the root of. In this case, the equation is and the variable X and X_n are involved. The initial 
guess is only for the variable X, but the equation depends on the value of X_n as well.

By using the args parameter, you can pass the value of X_n to the equation function along with the
 initial guess for X. In the example code:
root, = fsolve(equation, initial_guess, args=(initial_guess,))

The args=(initial_guess,) part is passing the initial guess for X_n to the equation function. Inside 
the equation function, you can access this value as args[0]. This way, you can use the Newton-Raphson 
method to iteratively solve for the root while updating both X and X_n in each iteration.
'''