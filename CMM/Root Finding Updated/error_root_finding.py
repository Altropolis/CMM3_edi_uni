# Purpose of the Code:
# This Python script compares the Newton-Raphson method and the
# Secant method for finding roots of two different functions.

# It explores the behavior of these root-finding algorithms by
# varying the number of iterations and plots the solutions and errors against the iteration count.

# Importing necessary modules
import math
import numpy as np
import matplotlib.pyplot as plt

# Definition of function for Newton-Raphson method
def newton2(f, Df, x0, N):
    """
    Newton-Raphson method for finding the root of a function.

    :param f: Function for which to find the root.
    :param Df: Derivative of the function.
    :param x0: Initial guess.
    :param N: Maximum number of iterations.
    :return: Approximated root.
    """
    xn = x0
    for n in range(0, N):
        fxn = f(xn)
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn / Dfxn
    return xn

# Definition of function for the Secant method
def secant(f, a, b, N):
    """
    Secant method for finding the root of a function.

    :param f: Function for which to find the root.
    :param a: Initial guess (left endpoint).
    :param b: Initial guess (right endpoint).
    :param N: Maximum number of iterations.
    :return: Approximated root.
    """
    if f(a) * f(b) >= 0:
        print("Secant method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1, N + 1):
        m_n = a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))
        f_m_n = f(m_n)
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
            print("Secant method fails.")
            return None
    return a_n - f(a_n) * (b_n - a_n) / (f(b_n) - f(a_n))

# Main Program
n_max = 20

n_array_N = np.zeros(n_max - 1)
sol_array_N = np.zeros(n_max - 1)
fun_array_N = np.zeros(n_max - 1)

n_array_S = np.zeros(n_max - 1)
sol_array_S = np.zeros(n_max - 1)
fun_array_S = np.zeros(n_max - 1)

# Function 1: x^2 + 4*x - 12
f1 = lambda x: x ** 2 + 4 * x - 12
df1 = lambda x: 2 * x + 4

# Initial guesses for Newton and Secant methods
x0_f1 = 1
a_f1, b_f1 = 1, 3

for i in range(1, n_max):
    # Newton method for Function 1
    solution = newton2(f1, df1, x0_f1, i)
    n_array_N[i - 1] = i
    sol_array_N[i - 1] = solution
    fun_array_N[i - 1] = np.absolute(f1(solution))

    # Secant method for Function 1
    solution = secant(f1, a_f1, b_f1, i)
    n_array_S[i - 1] = i
    sol_array_S[i - 1] = solution
    fun_array_S[i - 1] = np.absolute(f1(solution))

# Plotting for Function 1
plt.figure()
plt.plot(n_array_N, sol_array_N, '-o', n_array_S, sol_array_S, '-o')
plt.xlabel("Number of iterations")
plt.ylabel("Solution")
plt.title("Root Finding: Function 1")
plt.xlim(0, n_max)

plt.figure()
plt.semilogy(n_array_N, fun_array_N, '-o', n_array_S, fun_array_S, '-o')
plt.semilogy(n_array_S, np.exp(-2.0 * n_array_S), label=r'$e^{-2.0n}$')
plt.semilogy(n_array_S, np.exp(-2.5 * n_array_S), label=r'$e^{-2.5n}$')
plt.xlabel("Number of iterations")
plt.ylabel("Error, defined as |f(solution)|")
plt.title("Error Convergence: Function 1")
plt.xlim(0, n_max)
plt.legend()

# Function 2: sin(x) * exp(x^0.1)
f2 = lambda x: math.sin(x) * math.exp(x ** 0.1)
df2 = lambda x: (math.exp(x ** 0.1) * math.sin(x)) / (10 * x ** (9 / 10)) + math.exp(x ** 0.1) * math.cos(x)

# Initial guesses for Newton and Secant methods
x0_f2 = 4
a_f2, b_f2 = 1, 4

for i in range(1, n_max):
    # Newton
