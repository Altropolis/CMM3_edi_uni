import math

def bisection(f, a, b, N):
    '''
    Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    Example 1:
    >>> f = lambda x: x**2 - x - 1
    >>> bisection(f, 1, 2, 25)
    1.618033990263939

    Example 2:
    >>> f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f, 0, 1, 10)
    0.5
    '''

    # Check if the signs of f(a) and f(b) are the same, indicating a possible failure
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None

    # Initialize interval values
    a_n = a
    b_n = b

    # Perform the bisection method for N iterations
    for n in range(1, N + 1):
        # Calculate the midpoint of the current interval
        m_n = (a_n + b_n) / 2
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
            print("Bisection method fails.")
            return None

    # Return the midpoint of the final interval after N iterations
    return (a_n + b_n) / 2

# Define the function f(x) for which we are trying to find a root
# f = lambda x: x - (1.325 / (math.log((0.000005 / 3.7 * 0.005) + 5.74 / 13.473**0.9))**2)
f = lambda x: 1 / (x**0.5) + 2.0 * math.log((0.0000015 / 3.7 * 0.005) + (2.531 / 13.743 * (x**0.5)))

# Use the bisection method to approximate a root within the specified interval and iterations
approx_phi = bisection(f, 0.01, 0.08, 25)

# Print the result of the approximation
print(approx_phi)
