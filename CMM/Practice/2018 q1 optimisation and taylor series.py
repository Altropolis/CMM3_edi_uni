# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:25:20 2023

@author: blath
"""
'''
For these conditions, determine the optimum values of d and t for which design
buckling stress is no higher than 80% of the maximum buckling stress of the pipe
material, but for which material cost is still as low as possible.
'''

from scipy.optimize import minimize_scalar, Bounds


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

def I_func(d, t):
    d_i = d-t
    d_o = d    
    return (pi/4)*(d_o**4 - d_i**4)

I_for_max = I_func(d1, t1)
print('I for max calc is:', I_for_max)    

def max_stress(d, t):
    return (pi*E*I_for_max/((H**2)*d*t))

max_sigma_b = max_stress(d1, t1)

print('The max buckling stress is:', max_sigma_b)                          


def opt_stress(d, t):
    Area = ((pi*(d)**2)/4) - ((pi*(d - t)**2)/4)
    Force = P
    stress = Force/Area
    return 0.8*max_sigma_b - stress

#Want to minimise as we want lowest cost
d_bounds = (d1, d2)
t_bounds = (t1, t2)

result = minimize_scalar(lambda d: minimize_scalar(lambda t: opt_stress(d, t), bounds=t_bounds).fun, bounds=d_bounds)

optimal_d = result.x
optimal_t = minimize_scalar(lambda t: opt_stress(optimal_d, t), bounds=t_bounds).x

print("Optimal d:", optimal_d)
print("Optimal t:", optimal_t)

Area_opt = ((pi*(optimal_d + optimal_t)**2)/4) - ((pi*(optimal_d)**2)/4)
weight = (Area_opt*H)*rho
print(f'The weight of the optimal pipe is: {weight}kg')
cost = weight*coeff_w + coeff_diam*optimal_d
print(f'The cost of the optimal pipe is; £{cost}')

'''                          
def stress(vars):
    vars = d, t
    d_i = d
    d_o = d+t
    I = I_func(d, t)
    sigma_b = max_sigma_b
    return (pi*E*I)/((H**2)*d*t) - 0.8*sigma_b_val

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
    vars = d, t
    return (pi*E*I_for_max/((H**2)*d*t))
'''

