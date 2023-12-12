# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:06:44 2023

@author: s2192747
"""

# Import the numpy library for numerical operations

import numpy as np

 

# Define the Newton-Raphson function for root finding

def NewtonRaph2(f, Df, x0, epsilon, max_iter):

    xn = x0  # Initial guess for the root

    # Iterate up to a maximum number of times

    for n in range(0, max_iter):

        fxn = f(xn)  # Evaluate the function at the current guess

        # Check if the current function value is within the desired tolerance

        if abs(fxn) < epsilon:

            print('Found solution after ', n, ' iterations.')

            return (xn)  # Return the current guess as the root

        Dfxn = Df(xn)  # Evaluate the derivative at the current guess

        # Check if the derivative is zero (to avoid division by zero)

        if Dfxn == 0:

            print('Zero derivative. No solution found.')

            return None

        # Update the current guess using the Newton-Raphson formula

        xn = xn - (fxn / Dfxn)

    # If the loop completes without returning, maximum iterations were exceeded

    print('Exceeded maximum iterations. No solution found.')

    return None

# Initial guess for the root

x0 = 1

# Tolerance for the solution

epsilon = 1e-9

# Maximum number of iterations

max_iter = 100

# Function for which the root is to be found

f = lambda x: x**4+5*x**3+15*x**2+3*x-10

# Derivative of the function

Df = lambda x: 4*x**3+15*x**2+30*x+3

# Call the Newton-Raphson function and store the solution

solution2 = NewtonRaph2(f, Df, x0, epsilon, max_iter)

# Print the solution

print(solution2)

# Define a function ply_iter to perform polynomial deflation

def ply_iter(A, t):

    """

    Compute the quotient q(x) = p(x) / (x - t) and residual remainder.

    Parameters:

    A - numpy array containing coefficients of p(x) in decreasing order of power.

    t - the value of x for which p(x) is divided.

    Returns:

    q - array of coefficients for the quotient polynomial q(x).

    r - residual value after division.

    """

    # Determine the degree of the polynomial (length of A - 1)

    n = len(A) - 1

    # Initialize an array of zeros for storing coefficients of q(x)

    q = np.zeros(n, dtype=np.float64)

    # Initialize the remainder (r) as the last element of A

    r = A[n]

    # Iterate over the coefficients of A in reverse order

    for a in reversed(range(n)):

        # Assign the current coefficient to s

        s = A[a]

        # Update the current position in q with the remainder

        q[a] = r

        # Update the remainder for the next iteration

        r = s + r * t

    # Return the quotient array and the final remainder

    return q, r 

# Test the function

# Define an array A with coefficients of the polynomial p(x)

A = np.array([-10, 3, 15, 5, 1])

# Define the value of t for division

t = solution2

# Call the ply_iter function and store its output in quotient and residual

quotient, residual = ply_iter(A, t)

# Print the original coefficients of the polynomial p(x)

print('Coeffs a0, a1, a2, ..., an:', A)

# Print the coefficients of the quotient polynomial q(x)

print('of quotient a0+a1*x+a2*x^2+...an*x^n:', quotient)

# Print the residual value after division

print('Residual:', residual)

# Import the numpy library for numerical operations

import numpy as np

import sympy as sym

# Define the Newton-Raphson function for root finding

def NewtonRaph3(f, Df, x0, epsilon, max_iter):

    xn = x0  # Initial guess for the root

    # Iterate up to a maximum number of times

    for n in range(0, max_iter):

        fxn = f(xn)  # Evaluate the function at the current guess

        # Check if the current function value is within the desired tolerance

        if abs(fxn) < epsilon:

            print('Found solution after ', n, ' iterations.')

            return (xn)  # Return the current guess as the root

        Dfxn = Df(xn)  # Evaluate the derivative at the current guess

        # Check if the derivative is zero (to avoid division by zero)

        if Dfxn == 0:

            print('Zero derivative. No solution found.')

            return None

        # Update the current guess using the Newton-Raphson formula

        xn = xn - (fxn / Dfxn)

    # If the loop completes without returning, maximum iterations were exceeded

    print('Exceeded maximum iterations. No solution found.')

    return None

a0=quotient[0]

a1=quotient[1]

a2=quotient[2]

a3=quotient[3]

print(quotient[0])

# Initial guess for the root

x0 = 1

# Tolerance for the solution

epsilon = 1e-9

# Maximum number of iterations

max_iter = 100

# Function for which the root is to be found

f = lambda x: a3*x**3+a2*x**2+a1*x+a0

# Derivative of the function

Df = lambda x: a3*3*x**2+a2*2*x+a1

# Call the Newton-Raphson function and store the solution

solution3 = NewtonRaph2(f, Df, x0, epsilon, max_iter)

# Print the solution

print(solution3)

print('Roots are: ', solution3, solution2)