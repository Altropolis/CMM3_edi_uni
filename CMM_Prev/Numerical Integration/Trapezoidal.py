'''
    Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.
'''
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

# Generating a plot of the function y = e^(-x^2)
x = np.linspace(-0.5, 1.5, 100)
y = np.exp(-x**2)
plt.plot(x, y)

# Highlighting the area under the curve between x=0 and x=1
x0 = 0; x1 = 1;
y0 = np.exp(-x0**2); y1 = np.exp(-x1**2);
plt.fill_between([x0, x1], [y0, y1])

plt.xlim([-0.5, 1.5]); plt.ylim([0, 1.5]);
plt.show()

# Calculating the area of the trapezoid formed by connecting (x0, y0) and (x1, y1)
A = 0.5 * (y1 + y0) * (x1 - x0)
print("Trapezoid area:", A)

def trapz(f, a, b, N=1000):
    '''Approximate the integral of f(x) from a to b by the trapezoid rule.

    The trapezoid rule approximates the integral \int_a^b f(x) dx by the sum:
    (dx/2) \sum_{k=1}^N (f(x_k) + f(x_{k-1}))
    where x_k = a + k*dx and dx = (b - a)/N.

    Parameters
    ----------
    f : function
        Vectorized function of a single variable
    a , b : numbers
        Interval of integration [a,b]
    N : integer
        Number of subintervals of [a,b]

    Returns
    -------
    float
        Approximation of the integral of f(x) from a to b using the
        trapezoid rule with N subintervals of equal length.

    Examples
    --------
    >>> trapz(np.sin,0,np.pi/2,1000)
    0.9999997943832332
    '''
    # Discretizing the interval [a, b] into N subintervals
    x = np.linspace(a, b, N+1)
    # Calculating function values at each endpoint
    y = f(x)
    y_right = y[1:]  # right endpoints
    y_left = y[:-1]  # left endpoints
    dx = (b - a) / N
    # Applying the trapezoid rule formula to estimate the integral
    T = (dx/2) * np.sum(y_right + y_left)
    return T
