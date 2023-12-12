#Euler's method is a basic numerical approach for solving ordinary differential equations (ODEs)
# by approximating the solution at discrete steps. It estimates the slope at each point and uses
# it to predict the next value. While simple and computationally efficient, it is a first-order method,
# limiting its accuracy for complex or stiff systems. Euler's method is suitable when computational
# resources are constrained or a quick approximation suffices. In contrast, the Fourth Order Runge-Kutta
# method provides higher accuracy, making it preferable for precision-critical applications or intricate systems.


# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    dydx = 10*y**2-y**3
    return dydx

# initial conditions
x0 = 0
y0 = 0.02
# total solution interval
x_final = 10
# step size
h = 0.01
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
n_exact = 1000
x_exact = np.linspace(0,x_final,n_exact+1)
y_exact = np.zeros(n_exact+1)

# exact values of the solution
# for i in range(n_exact+1):
#     y_exact[i] = y0 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# # print results on screen
# print ('Solution: step x y-eul y-exact error%')
# for i in range(n_step+1):
#     print(i,x_eul[i],y_eul[i], y0 * math.exp(-x_eul[i]),
#             (y_eul[i]- y0 * math.exp(-x_eul[i]))/
#             (y0 * math.exp(-x_eul[i])) * 100)
# # ------------------------------------------------------

# ------------------------------------------------------
# # print results in a text file (for later use if needed)
# file_name= 'output_h' + str(h) + '.dat'
# f_io = open(file_name,'w')
# for i in range(n_step+1):
#     s1 = str(i)
#     s2 = str(x_eul[i])
#     s3 = str(y_eul[i])
#     s4 = s1 + ' ' + s2 + ' ' + s3
#     f_io.write(s4 + '\n')
# f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_eul, y_eul , 'b.-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


