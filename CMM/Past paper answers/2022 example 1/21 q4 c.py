# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:07:54 2023

@author: s2192747
"""

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

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
# List of step sizes
h_values = [0.025, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3]

for h in h_values:

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
    print('h   step   x   y-eul   y-exact  error%')
    for i in range(n_step+1):
    
        rounded_x_eul = round(x_eul[i], 5)  # adjust the number of decimal places as needed
        rounded_y_eul = round(y_eul[i], 5)
        rounded_y_exact = round(y_exact[i], 5)
        rounded_abs_error = round(abs_error[i], 5)
        rounded_error = round(error[i], 5)

        # print(i, rounded_x_eul, rounded_y_eul, rounded_y_exact, rounded_abs_error, rounded_error)
        
    # Plotting
    plt.plot(x_eul, y_eul, 'b.-', label='Euler Method')
    plt.plot(x_exact, y_exact, 'r-', label='Exact Solution')
    plt.xlabel('x')
    plt.ylabel('y(x)')
    plt.title(f'Euler Method with h={h}')
    plt.legend()
    plt.show()

# ------------------------------------------------------
 # for i in range(1):
    t1 = int(2*np.pi/h)  # Convert to integer index
    t2 = int(4*np.pi/h)  # Convert to integer index

    
    print(h, t1, np.round(x_eul[t1],5), y_eul[t1], error[t1])
    print(h, t2, np.round(x_eul[t2],5), y_eul[t2], error[t2])
    
    # # Sample data
    # data = {'Name': ['John', 'Alice', 'Bob'],
    #         'Age': [25, 30, 22],
    #         'City': ['New York', 'San Francisco', 'Seattle']}

    # # Creating a DataFrame (table)
    # df = pd.DataFrame(data)

    # # Display the table
    # print(df)


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
