# The provided Python code employs the rectangle rule (midpoint rule) for numerical integration,
# estimating the definite integral of a given function within a specified interval.
# The rect_rule function divides the interval [a, b] into n subintervals, calculates the width of
# each subinterval (dx), evaluates the function at the midpoint of each subinterval, and sums up
# the areas of the resulting rectangles. This method offers a straightforward numerical integration
# approach suitable for quick estimates, especially in scenarios where more computationally expensive
# or accurate methods might be unnecessary. It serves as an introductory tool or a balance between
# accuracy and computational cost, although for more complex functions or higher precision, other
# methods like Simpson's rule or Gaussian quadrature might be preferable.









import numpy as np


def calculate_dx(a, b, n):
    # Calculate the width of each rectangle
    return (b - a) / float(n)


def rect_rule(f, a, b, n):
    total = 0.0
    dx = calculate_dx(a, b, n)

    # Iterate over each rectangle
    for k in range(0, n):
        # Evaluate the function at the midpoint of the rectangle
        # Multiply by the width of the rectangle and accumulate the results
        total += f((a + (k * dx)))

    # Return the approximate integral value
    return dx * total


def f(x):
    # The function to be integrated
    return np.exp(-x ** 2)


# Call the rect_rule function with the specified function, interval, and number of rectangles
result = rect_rule(f, 0, 1, 1000)

# Print the result to the console
print(result)
