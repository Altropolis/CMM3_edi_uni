
# The provided implementation is a modification of the False Position Method (FPM) for solving equations.
# The unmodified FPM can suffer from slow convergence when one of the bounds remains unchanged through many iterations.
# To address this issue, a modification has been introduced by halving the function value at the 'stuck' bound if the algorithm
# detects that the bound has not moved after a certain number of steps.
# The specific modification involves multiplying the function value at the 'stuck' bound by 0.5 during the calculation of the new estimate.
# This adjustment aims to expedite convergence in cases where one bound appears to be 'stuck.'
# It's important to note that while this modification may improve convergence in certain scenarios, it deviates from the standard FPM, and its effectiveness should
# be carefully considered in the context of specific functions and convergence behaviors.


# Python3 implementation of Bisection
# Method for solving equations
import math

MAX_ITER = 1000


# An example function whose solution
# is determined using Bisection Method.
# The function is x^3 - x^2 + 2
def func(x):
    return (math.exp(-x) - 2)

# (x**2+4*x-19)

# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b, tol):
    if func(a) * func(b) >= 0:
        print("You have not assumed right a and b")
        return -1
    step = 0
    c = a  # Initialize result

    while step < MAX_ITER and abs(func(c)) > tol:
        # Find the point that touches x axis
        c = (a * 0.5 * func(b) - b * func(a)) / (0.5 * func(b) - func(a))

        # Check if the above found point is root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

        step += 1
    print("The value of root is : ", '%.4f' % c)
    print(step)


# Driver code to test above function
# Initial values assumed
a = -3
b = 30
tol = 1e-3
regulaFalsi(a, b, tol)
