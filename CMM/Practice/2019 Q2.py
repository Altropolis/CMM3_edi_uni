import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize

# Define the function to integrate
def integrand(x, p):
    return np.sin(x) * np.cos(p * x)

# Define the objective function (the integral to minimize)
def objective(p):
    result, _ = quad(integrand, 0, np.pi, args=(p,))
    return result

# Initial guess for the parameter p
initial_guess = 1.0

# Use the minimize function to find the optimal p
result = minimize(objective, initial_guess)

# Extract the optimal value of p
optimal_p = result.x[0]

# Print the result
print("Optimal p that minimizes the integral:", optimal_p)

import numpy as np
from scipy.optimize import minimize

import numpy as np
from scipy.optimize import minimize, fsolve

# Define the function to integrate
def integrand(x, p):
    return np.sin(x) * np.cos(p * x)

# Use the optimized value of p
optimal_p = result.x[0]

# Define a function to find zeros of the integrated function
def find_zeros(x):
    return integrand(x, optimal_p)

# Find zeros using root-finding (fsolve function from SciPy)
# We provide an initial guess of zeros within the [0, pi] range
initial_guess_zeros = np.linspace(0, np.pi, 10)
zeros = fsolve(find_zeros, initial_guess_zeros)

# Print the zeros
print("Values of x where the integrated function is zero:", zeros)

