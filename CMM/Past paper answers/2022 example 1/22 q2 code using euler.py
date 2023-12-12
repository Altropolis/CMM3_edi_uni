# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 17:42:32 2023

@author: s2086913
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dt
# i.e. the equation we want to solve: dy/dt = - y
def model(y,t):
    dydt = (10 * y**2 - y**3)
    return dydt

# initial conditions
t0 = 0
y0 = 0.02
# total solution interval
t_final = 10
# step size
h = 0.01
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(t_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
t_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
t_eul[0] = t0 

# Populate the t array
for i in range(n_step):
    t_eul[i+1] = t_eul[i] + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i], t_eul[i]) 
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print('Solution: step t y-eul')
print(400, t_eul[400], y_eul[400])
print(500, t_eul[500], y_eul[500])
# print(1000, t_eul[1000], y_eul[1000])
    
# ------------------------------------------------------

# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name = 'output_h' + str(h) + '.dat' 
f_io = open(file_name, 'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(t_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(t_eul, y_eul, 'b.-')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
# ------------------------------------------------------
