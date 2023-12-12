import numpy as np
from scipy.optimize import minimize

# Given table of theta values (in degrees) and corresponding radius values
theta_values = np.radians([-30, 0, 30])
radius_values = np.array([6870, 6728, 6615])

# Define the objective function to minimize
def objective(params):
    C, e, alpha = params
    computed_radii = C / (1 + e * np.sin(theta_values + alpha))
    difference = computed_radii - radius_values
    return np.sum(difference**2)

# Initial guess for parameters
initial_guess = [7000, 0.1, 0]

# Perform the minimization
result = minimize(objective, initial_guess, method='Nelder-Mead')

# Extract the optimized parameters
C_opt, e_opt, alpha_opt = result.x

# Calculate the smallest radius using the optimized parameters
smallest_radius = C_opt / (1 + e_opt * np.sin(theta_values + alpha_opt))

# Print the result
print("Optimized Parameters (C, e, alpha):", C_opt, e_opt, alpha_opt)
print("Smallest Radius:", smallest_radius)
