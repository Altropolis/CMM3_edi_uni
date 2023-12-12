# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 12:08:23 2023

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
    k= - 10
    dydx = k * y + (1 - k) * np.cos(x) - (1 + k) * np.sin(x)
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 4*np.pi
# step size
h = 0.1

# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply Euler method n_step times
for i in range(n_step):
    # compute the slope using the differential equation
    slope = model(y_eul[i],x_eul[i]) 
    # use the Euler method
    y_eul[i+1] = y_eul[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# super refined sampling of the exact solution 
# n_exact linearly spaced numbers
# only needed for plotting reference solution

# Definition of array to store the exact solution
n_exact = n_step
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)
abs_error = np.zeros(n_exact+1)
error = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = np.sin(x_exact[i]) + np.cos(x_exact[i])
    abs_error[i] = ((y_eul[i] - y_exact[i]))
    error[i] = (abs_error[i] /  y_exact[i]) * 100
                
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
# print results on screen
print('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    
    rounded_x_eul = round(x_eul[i], 5)  # adjust the number of decimal places as needed
    rounded_y_eul = round(y_eul[i], 5)
    rounded_y_exact = round(y_exact[i], 5)
    rounded_abs_error = round(abs_error[i], 5)
    rounded_error = round(error[i], 5)

    print(i, rounded_x_eul, rounded_y_eul, rounded_y_exact, rounded_abs_error, rounded_error)

# ------------------------------------------------------
 # for i in range(1):
t1 = int(2*np.pi/h)  # Convert to integer index
t2 = int(4*np.pi/h)  # Convert to integer index

    
print(t1, np.round(x_eul[t1],5), y_eul[t1])
print(t2, np.round(x_eul[t2],5), y_eul[t2])

'''
# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output_h' + str(h) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------
'''
# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


