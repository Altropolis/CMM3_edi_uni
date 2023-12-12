"""
The Secant method is a root-finding algorithm that iteratively refines an initial guess to approximate
the root of a real-valued function. This modified Secant method introduces a relaxation coefficient
`alpha` to adjust the step size in each iteration, providing more flexibility in handling different
functions and convergence behaviors. The algorithm computes a full Secant step using both the current
and previous function values, enhancing accuracy.

Usage:
The modified Secant method can be advantageous when the convergence behavior of
the original Secant method is sensitive to step sizes or when the initial guess is far
from the actual root. The relaxation coefficient `alpha` allows users to adapt the step size
dynamically, potentially improving convergence in cases where the original method might struggle.

Original vs. Modified:
Compared to the original Secant method, this modified version provides
additional control through the relaxation coefficient. The adjustment in
step size helps mitigate convergence issues and allows for more efficient convergence
 in certain scenarios. Users can experiment with different values of `alpha` to find the
 optimal balance between step size and convergence speed for their specific functions.
"""


def secant_method(func, x0, alpha=1.0, tol=1E-9, maxit=200):
    """
    Uses the secant method to find f(x)=0.
    INPUTS
    * func : function f(x)
    * x0 : initial guess for x
    * alpha : relaxation coefficient: modifies Secant step size
    * tol : convergence tolerance
    * maxit : maximum number of iterations, default=200
    """

    # Initialize variables
    x, xprev = x0, 1.001 * x0
    f, fprev = x**4 - x - 1, xprev**4 - xprev - 1
    rel_step = 2.0 * tol
    k = 0

    # Output table headers
    print('{0:12} {1:12} {2:12} {3:12} {4:12}'.format('Iteration', 'x', 'f(x)', 'Rel step', 'alpha * Delta x'))

    # Main loop for iterations
    while (abs(f) > tol) and (rel_step > tol) and (k < maxit):
        # Compute relative step size
        rel_step = abs(x - xprev) / abs(x)

        # Full secant step
        dx = -f / (f - fprev) * (x - xprev)

        # Update `xprev` and `x` simultaneously
        xprev, x = x, x + alpha * dx

        # Update `fprev` and `f`
        fprev, f = f, func(x)

        # Print iteration information
        print('{0:10d} {1:12.5f} {2:12.5f} {3:12.5f} {4:12.5f}'.format(k, xprev, fprev, rel_step, alpha * dx))

        # Increment iteration counter
        k += 1

    # Return the final approximation of the root
    return x

# Example usage of the secant method
func = lambda x: x**4 - x - 1
solution = secant_method(func, 0.0001, alpha=1.0, tol=1E-9, maxit=200)
print("Approximate root:", solution)