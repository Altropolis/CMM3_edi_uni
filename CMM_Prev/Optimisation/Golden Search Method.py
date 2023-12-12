


import numpy as np

def golden_section_search(ftn, a, b, tol=1e-9):
    """
    Golden section search algorithm to find the minimum of a unimodal function.

    Parameters:
    - ftn: The function to minimize.
    - a, b: Initial interval [a, b] where the minimum is assumed to exist.
    - tol: Tolerance for terminating the algorithm when (b - a) <= tol.

    Returns:
    - The x-coordinate of the minimum within the interval.

    Notes:
    - Assumes that ftn is a unimodal function within the specified interval.
    """

    # Golden ratio minus one
    gr1 = (np.sqrt(5) - 1) / 2

    # Initial points within the interval
    x1 = b - gr1 * (b - a)
    x2 = a + gr1 * (b - a)

    # Evaluate the function at initial points
    f1 = ftn(x1)
    f2 = ftn(x2)

    # Continue refining until the interval width is less than the tolerance
    while (b - a) > tol:
        #For minimisation change to f1 <= f2:
        if f1 >= f2:
            # If the function value at x1 is greater than or equal to x2, update the interval and x1
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - gr1 * (b - a)
            f1 = ftn(x1)
        else:
            # If the function value at x2 is greater than x1, update the interval and x2
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + gr1 * (b - a)
            f2 = ftn(x2)

    # Return the x-coordinate of the minimum within the interval
    return (a + b) / 2

# Example usage of the function
a = 6
b = 9

# Define the function to minimize
def ftn(x):
    return 2 * np.sin(x) - (x**2) / 10

# Run the golden section search algorithm and display the result
result = golden_section_search(ftn, a, b, tol=1e-9)

# Print the result
print("Result of the golden section search algorithm:", result)
