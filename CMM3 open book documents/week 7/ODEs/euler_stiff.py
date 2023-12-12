# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    dydx = -1000.0*y + 3000.0 - 2000.0*math.exp(-x)
    #dydx = 3000.0 - 2000.0*math.exp(-x)
    return dydx

# initial conditions
x0 = 0
y0 = 0
# total solution interval
x_final = 0.3

# Change step size at x=x2
x2 = 0.01
# step size for x<x2
h1 =  0.0002  
# increased step size for x>x2
h2 = 0.0021

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

# ------------------------------------------------------
# super refined sampling of the exact solution c*e^(-x)
# n_exact linearly spaced numbers
# only needed for plotting reference solution

# Definition of array to store the exact solution
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1) 
y_exact = np.zeros(n_exact+1)

# exact values of the solution
for i in range(n_exact+1):
    y_exact[i] = 3.0 - 0.998 * math.exp(-1000*x_exact[i]) - 2.002 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output' + str(h1) + '_' + str(h2) + '.dat' 
f_io = open(file_name,'w') 
for i in range(n_step+1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# print results in a text file (for later use if needed)
file_name= 'output_exact.dat' 
f_io = open(file_name,'w') 
for i in range(n_exact+1):
    s1 = str(i)
    s2 = str(x_exact[i])
    s3 = str(y_exact[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


