# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:54:06 2023

@author: s2086913
"""


# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    dydx = 10*y**2 - y**3
    return dydx

# initial conditions
x0 = 0
y0 = 0.02
# total solution interval
x_final = 10

# Change step size at x=x2
x2 = 0.01
# step size for x<x2
h1 =  0.0005
# increased step size for x>x2
h2 = 0.0005

h = h1
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(x2/h1) + math.ceil((x_final-x2)/h2)

#n_step = 16

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    if x_eul[i]>x2:
        x_eul[i+1]  = x_eul[i]  + h2
    else:
        x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i],x_eul[i]) 
    # change step after a certain x=x2
    if x_eul[i]>x2:
        h=h2
    else:
        h=h1
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  

# ------------------------------------------------------
# Print the value of y(x) at x = 4
x_at_4_index = np.abs(x_eul - 4).argmin()
y_at_4 = y_eul[x_at_4_index]
print("y(4) =", y_at_4)
# ------------------------------------------------------
# Print the value of y(x) at x = 5
x_at_5_index = np.abs(x_eul - 5).argmin()
y_at_5 = y_eul[x_at_5_index]
print("y(5) =", y_at_5)
# ------------------------------------------------------
#Print the value of y(x) at x = 10
x_at_10_index = np.abs(x_eul - 10).argmin()
y_at_10 = y_eul[x_at_10_index]
print("y(10) =", y_at_10)
# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------