# import numpy as np
# from scipy.optimize import minimize
# import numpy as np
# # Define the objective function without constraints
# E = 200
# H = 2.75
# rho = 7800
# I = np.pi/2 * ((d/2+t)**4-(d/2)**4)
# def objective(X):
#     d,t = X
#     return np.pi*E*I/(H**2*d*t)
#
# # Define the equality constraint function with a Lagrange multiplier (lambda)
# def eq(X):
#     d,t = X
#     # Define the equality constraint 2x - y + z = 3
#     return d*0.9 + (0.7*(H*(np.pi*(d/2+t)**2 - (d/2)**2))*rho),x
#
# # Use the minimize function from SciPy to find the solution
# # The optimization problem includes the objective function and the equality constraint
# # The initial guess for optimization is [1, 4, 5]
# sol = minimize(objective, [1, 4, 5], constraints={'type': 'eq', 'fun': eq})
#
# # Print the optimization result
# print(sol)

import numpy as np
from scipy.optimize import minimize

# Given data
P = 20.0  # kN
E = 200.0 * 1e9  # Pa (200 GPa)
H = 2.75  # m
density = 7800.0  # kg/m^3
g = 9.81  # m/s^2 (acceleration due to gravity)
max_buckling_stress = np.pi * E / H**2

# Cost coefficients
cost_weight_coefficient = 0.7  # £/kg
cost_diameter_coefficient = 0.9  # £/m

# Design variables
d_min = 0.01  # m (1 cm)
d_max = 0.1  # m (10 cm)
t_min = 0.001  # m (0.1 cm)
t_max = 0.01  # m (1 cm)

# Buckling stress constraint
def buckling_stress_constraint(x):
    d, t = x
    I = np.pi * (d**4 - (d - 2*t)**4) / 64.0  # Second moment of area for a hollow cylinder
    omega = np.pi * E * I / (H**2 * d * t)
    return 0.8 * max_buckling_stress - omega

# Cost function to minimize
def cost_function(x):
    d, t = x
    W = density * np.pi * (d**2 - (d - 2*t)**2) * H * g / 4.0
    cost = cost_weight_coefficient * W + cost_diameter_coefficient * np.pi * d * H
    return cost

# Initial guess
initial_guess = [(d_min + d_max) / 2, (t_min + t_max) / 2]

# Bounds for d and t
bounds = [(d_min, d_max), (t_min, t_max)]

# Constraint bounds
constraint_bounds = {'type': 'ineq', 'fun': buckling_stress_constraint}

# Optimization
result = minimize(cost_function, initial_guess, bounds=bounds, constraints=constraint_bounds)

# Extract the optimized values
optimal_d, optimal_t = result.x
optimal_cost = result.fun

# Print the result
print("Optimal Diameter (m):", optimal_d)
print("Optimal Thickness (m):", optimal_t)
print("Optimal Cost (£):", optimal_cost)
