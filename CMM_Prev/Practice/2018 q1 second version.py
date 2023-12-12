# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 20:20:52 2023

@author: blath
"""

from scipy.optimize import minimize

P = 20e3 #kN
coeff_w = 0.7
coeff_diam = 0.9
E = 200e9 # GPa
H = 2.75
rho = 7800
pi = 3.14159

#pipe available diameters:
d1 = 1e-2
d2 = 10e-2

#Thicknesses:
t1 = 0.1e-2 
t2 = 1e-2

def objective_cost(vars):
    d, t = vars
    Area_opt = ((pi*(d)**2)/4) - ((pi*(d - t)**2)/4)
    weight = (Area_opt*H)*rho
    return weight*coeff_w + coeff_diam*d

def I_func(vars):
    d, t = vars
    d_i = d-t
    d_o = d    
    return (pi/4)*(d_o**4 - d_i**4)
#Going to assume stress to be force over area
#Because we're given a force
def max_stress(vars):
    d, t = vars
    return (pi*E*I_func(vars)/((H**2)*d*t))

def stress(vars):
    d, t = vars
    return 0.8*max_stress(vars)

d_bounds = (d1, d2)
t_bounds = (t1, t2)


# Constraints
stress_constraint = {'type': 'ineq', 'fun': lambda vars: stress(vars) - max_stress(vars)}
bounds = [d_bounds, t_bounds]

# Initial guess
initial_guess = [(d1 + d2) / 2, (t1 + t2) / 2]  # Choose initial values within the bounds

# Optimization
result = minimize(objective_cost, initial_guess, method='SLSQP', bounds=bounds, constraints=[stress_constraint])

# Extract the optimized values
optimal_d, optimal_t = result.x

# Calculate the cost
cost = result.fun

print('The optimised vals for the pipe are:')
print(f'Optimal d: {optimal_d}m')
print(f'Optimal t: {optimal_t}m')


print(f'The cost of the optimal pipe is; £{cost}')
