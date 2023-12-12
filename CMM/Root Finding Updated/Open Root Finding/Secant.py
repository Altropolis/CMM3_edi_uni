
# The Secant method is a numerical technique for finding roots of real-valued functions.
# Unlike methods that require the computation of derivatives, the Secant method approximates
# the derivative using finite differences. This makes it applicable to functions where
# derivatives are challenging to compute. The method iteratively refines the interval
# [a, b] based on the intersection of the secant line with the x-axis. The process continues
# until the function value is sufficiently close to zero or the maximum number of iterations
# is reached. The Secant method is versatile and can handle a wider range of initial guesses,
# making it useful when the initial approximation is not close to the actual root.

import math
def secant(f, a, b, N):
    '''Approximate solution of f(x)=0 on interval [a,b] by the secant method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a, b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    m_N : number
        The x intercept of the secant line on the Nth interval
            m_n = a_n - f(a_n)*(b_n - a_n)/(f(b_n) - f(a_n))
        The initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0
        for some intercept m_n, then the function returns this solution.
        If all signs of values f(a_n), f(b_n), and f(m_n) are the same at any
        iteration, the secant method fails and returns None.

    Examples
    --------
    >>> f = lambda x: x**2 - x - 1
    >>> secant(f, 1, 2, 5)
    1.6180257510729614
    '''
    # Check if the signs of f(a) and f(b) are the same
    if f(a) * f(b) >= 0:
        print("Secant method fails. The signs of f(a) and f(b) must be different.")
        return None

    # Initialize the endpoints of the interval
    a_n = a
    b_n = b

    for n in range(1, N + 1):
        # Secant method formula to find the next approximation
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

        # Evaluate the function at the new approximation
        f_m_n = f(m_n)

        # Update the interval based on the signs of f(a_n), f(b_n), and f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Secant method fails. The signs of f(a_n), f(b_n), and f(m_n) are the same.")
            return None

    # Return the final approximation of the root
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))


# Example usage of the secant method
f = lambda x: 1 / (x ** 0.5) + 2.0 * math.log((0.0000015 / 3.7 * 0.005) + (2.531 / 13, 743 * (x ** 0.5)))
solution = secant(f, 0.01, 0.08, 25)
print("Approximate root:", solution)
