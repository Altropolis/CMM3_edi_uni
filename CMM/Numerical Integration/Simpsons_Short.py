# This code defines a Python function, simps, which implements Simpson's rule for numerical integration.
# Simpson's rule is a numerical technique for approximating definite integrals by dividing the integration
# interval into small subintervals and using quadratic interpolations for each subinterval. The simps function
# takes as input a user-defined function to be integrated, along with the integration limits and the number
# of intervals. It then applies Simpson's rule to calculate an approximate value for the integral. This method
# can be useful for functions with moderate smoothness, providing better accuracy than simpler methods like
# the trapezoidal rule. The code demonstrates its functionality by integrating an example function and
# printing the result. Users may choose to use this method over other numerical integral methods when
# dealing with functions that exhibit oscillatory behavior or when a more accurate approximation is desired.



import numpy as np


def simps(f, a, b, N=50):
    # Check if N is even (required for Simpson's rule)
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")

    # Calculate the step size
    dx = (b - a) / N

    # Generate an array of x-values
    x = np.linspace(a, b, N + 1)

    # Evaluate the function at each x-value to get y-values
    y = f(x)

    # Apply Simpson's rule formula to calculate the approximate integral
    S = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    # Print the result
    print(S)

    # Return the approximate integral
    return S


# Define the function to be integrated (exp(x**-2))
f = lambda x: np.exp(x ** -2)

# Call the simps function with the given function, integration limits (1 to 2), and number of intervals (24)
solution = simps(f, 1, 2, 1000)

# Print the result
print(solution)
