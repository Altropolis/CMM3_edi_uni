"""
The Inverse Quadratic Interpolation method offers a robust approach to root finding,
particularly when dealing with functions that may not exhibit smooth behavior or when the
convergence behavior of other methods is suboptimal. Also, the functions need to be of order 3 or higher
and is better than linear secant methods as the estimating curve better fits the
function than the linear estimating line of the secant method.
It is advantageous when the initial guesses are close to the true root, as it tends to converge rapidly.

The method works by constructing an interpolating polynomial based on three points and then solving for the root of the polynomial.
By iteratively updating the three points, the algorithm refines its approximation of the root.
This adaptability makes it useful in scenarios where other methods may struggle, and the method often
demonstrates efficiency in terms of convergence speed with proper initial guesses.
"""
import matplotlib.pyplot as plt
import numpy as np
def inverse_quadratic_interpolation(f, x0, x1, x2, max_iter=20000000, tolerance=1e-5):
    steps_taken = 0

    # Iterate until either the maximum number of iterations is reached or the difference between x1 and x0 is small enough
    while steps_taken < max_iter and abs(x1 - x0) > tolerance:
        fx0 = f(x0)  # Evaluate the function at x0
        fx1 = f(x1)  # Evaluate the function at x1
        fx2 = f(x2)  # Evaluate the function at x2

        # Calculate the three Lagrange interpolating polynomials
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))

        # Calculate the new approximation using the sum of the interpolating polynomials
        new = L0 + L1 + L2

        # Update the values of x0, x1, and x2 for the next iteration
        x0, x1, x2 = new, x0, x1

        steps_taken += 1  # Increment the iteration counter

    return x0, steps_taken


# Define the function for which we want to find the root
f = lambda x: x ** 3 + 2 * x ** 2 + 4 * x + 5

# Initial guesses for the root
root, steps = inverse_quadratic_interpolation(f, 4.3, 4.4, 4.5)

# Print the result
print("Root is:", root)
print("Steps taken:", steps)

# Plotting function and its root
x = np.linspace(-5,5,100)
y = f(x)
xest,yest = root, f(root)
plt.plot(xest, yest, marker="o", markersize=5)
plt.plot(x,y)
plt.show()