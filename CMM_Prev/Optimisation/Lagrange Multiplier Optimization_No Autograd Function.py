# This Python script utilizes the SciPy library to perform constrained optimization
# using the steepest descent method. The objective is to minimize the sum of squares
# of three variables (x, y, and z) subject to the equality constraint 2x - y + z = 3.
# The objective function and constraint function are defined, and the minimize function
# from SciPy is employed to find the optimal values of the variables. The code is
# particularly useful when dealing with optimization problems that involve equality
# constraints. The advantage of using this approach lies in the ability to handle
# constrained optimization problems efficiently. The minimize function automatically
# incorporates Lagrange multipliers to handle constraints, providing a convenient
# and effective way to find solutions that satisfy both the objective and the constraints.
# This method is especially valuable in engineering, finance, and various scientific
# fields where constraints on variables must be considered during the optimization process.



# Import necessary libraries
import numpy as np
from scipy.optimize import minimize

# Define the objective function without constraints
def objective(X):
    x, y, z = X
    return x**2 + y**2 + z**2

# Define the equality constraint function with a Lagrange multiplier (lambda)
def eq(X):
    x, y, z = X
    # Define the equality constraint 2x - y + z = 3
    return 2 * x - y + z - 3

# Use the minimize function from SciPy to find the solution
# The optimization problem includes the objective function and the equality constraint
# The initial guess for optimization is [1, 4, 5]
sol = minimize(objective, [1, 4, 5], constraints={'type': 'eq', 'fun': eq})

# Print the optimization result
print(sol)
