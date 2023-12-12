import math

# The following code implements the bisection method, a numerical technique for approximating the roots of
# a given continuous function within a specified interval. The method operates by iteratively narrowing down
# the interval where a root exists until the desired level of accuracy is achieved. The core idea relies on
# the intermediate value theorem, ensuring the existence of a root within an interval where the function
# changes sign. The bisection method is robust and reliable, especially when dealing with functions that are
# continuous and change sign within the specified interval. While it may converge more slowly than some
# other methods, it has the advantage of simplicity and stability, making it a suitable choice for various
# root-finding problems.

import math

def bisection(f, a, b, N):
    '''
    Approximate solution of f(x)=0 on the interval [a, b] by the bisection method.

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
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0, b_0] is given by [a, b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n), and f(m_n) are the same at any
        iteration, the bisection method fails and returns None.

    Examples
    --------
    f = lambda x: x**2 - x - 1
    bisection(f, 1, 2, 25)  # Example usage with a quadratic function

    f = lambda x: (2*x - 1)*(x - 3)
    bisection(f, 0, 1, 10)  # Example usage with a linear function
    '''

    # Check if the sign of f(a) is the same as the sign of f(b), which may indicate no solution in the interval
    if f(a) * f(b) >= 0:
        print("Bisection method fails. No guarantee of a solution in the given interval.")
        return None

    # Initialize variables for the interval endpoints
    a_n = a
    b_n = b

    # Perform bisection iterations
    for n in range(1, N + 1):
        m_n = (a_n + b_n) / 2  # Calculate the midpoint of the interval
        f_m_n = f(m_n)  # Evaluate the function at the midpoint

        # Adjust the interval based on the signs of f(a_n), f(b_n), and f(m_n)
        if f(a_n) * f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n) * f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found an exact solution.")
            return m_n
        else:
            print("Bisection method fails. The signs of f(a_n), f(b_n), and f(m_n) are the same.")
            return None
    return (a_n + b_n) / 2  # Return the midpoint of the final interval

# Example usage with a specific function f(x)
f = lambda x: 1 / (x**0.5) + 2.0 * math.log((0.0000015 / (3.7 * 0.005)) + (2.531 / 13743 * (x**0.5)))
approx_phi = bisection(f, 0.01, 0.08, 25)
print("mmmroximate solution:", approx_phi)
