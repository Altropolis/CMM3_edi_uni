# The code defines a function 'linearsolver' to solve a system of linear equations using Gaussian Elimination
# with Partial Pivoting and Backward Substitution. The function takes a coefficient matrix A and a column vector b
# as input and returns the solution vector x. This method is particularly useful for solving systems of linear
# equations when the number of equations equals the number of unknowns. Gaussian Elimination ensures the system
# is transformed to an upper triangular form, making it easier to find the solution. The code provides an example
# usage with a specific matrix A and vector b. You would use this code when you need to find the solution to a
# system of linear equations, common in various mathematical and engineering applications.

import numpy as np

def linearsolver(A, b):
    n = len(A)  # Get the size of the system (assuming A is a square matrix)

    # Initialize solution vector x with zeros
    x = np.zeros(n)

    # Create an augmented matrix by concatenating A and b.T (transposed to form a column vector)
    M = np.concatenate((A, b.T), axis=1)

    # Gaussian Elimination with Partial Pivoting
    for k in range(n):
        for i in range(k, n):
            # Partial pivoting: Swap rows if necessary
            if abs(M[i][k]) > abs(M[k][k]):
                M[[k, i]] = M[[i, k]]
            else:
                pass
            for j in range(k+1, n):
                # Perform row operations to eliminate elements below the diagonal
                q = M[j][k] / M[k][k]
                for m in range(n+1):
                    M[j][m] += -q * M[k][m]

    # Backward Substitution
    x[n-1] = M[n-1][n] / M[n-1][n-1]  # Solve for the last variable using backward substitution
    for i in range(n-2, -1, -1):
        z = M[i][n]
        for j in range(i+1, n):
            z = z - M[i][j] * x[j]
        x[i] = z / M[i][i]  # Backward substitution to find remaining variables

    return x

# Example Usage:
# A = np.array([[10., 15., 25], [4., 5., 6], [25, 3, 8]])
# b = np.array([[34., 25., 15]])
# print(linearsolver(A, b))

A = np.array([[70., 1., 0], [60., -1., 1.], [40, 0, -1]])
b = np.array([[636.7, 518.6, 307.4]])
print(linearsolver(A, b))
