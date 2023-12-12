import numpy as np

def poly_iter(A, t):
    # compute q(x) = p(x)/(x-t) and residual r
    # array A contains coefficients of p(x) 
    n = len(A) - 1
    # q: array of integers to store coefficients of q(x)
    q = np.zeros(n, dtype=np.int8)
    r = A[n]  # Initialize residual with the coefficient of the highest degree term

    # Iterate through the coefficients of p(x) in reverse order
    for a in reversed(range(n)):
        s = A[a]  # Coefficient of the current term in p(x)
        q[a] = r  # Coefficient of the current term in q(x)
        r = s + r * t  # Update the residual term

    # Print the results
    print('----------------------------------------')
    print('Coefficients a0, a1, a2, ..., an')
    print('of quotient a0 + a1*x + a2*x^2 + ... + an*x^n:')
    print(q)
    print('----------------------------------------')
    print('Residual:')
    print(r)
    print('----------------------------------------')

    return []  # Return an empty list (not needed for functionality)

# Example usage with a specific polynomial and divisor
A = np.array([-42, 0, -12, 1])
t = 3
poly_iter(A, t)
