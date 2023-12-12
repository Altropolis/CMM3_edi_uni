#The Runge-Kutta (RK) method is a family of iterative numerical techniques for solving ordinary
# differential equations (ODEs) by approximating the solution at discrete points. The Fourth Order
# Runge-Kutta (RK4) method, featured in this code, is a widely utilized variant known for its accuracy
# and simplicity. In RK4, the method proceeds through four sequential steps for each iteration: first,
# it estimates the slope at the current point using the original differential equation; second, it uses
# this slope to estimate the solution at the midpoint of the interval; third, it recalculates the slope at
# this midpoint; and finally, it combines the four slopes in a weighted average to compute an accurate estimate
# of the overall slope. This estimate is then used to update the solution.

# RK4 strikes a balance between accuracy and computational efficiency, making it a popular choice for solving
# ODEs in various scientific and engineering applications. Compared to simpler methods like Euler's method,
# RK4 provides more accurate results, especially for complex equations, making it preferable when precision
# is crucial or when dealing with stiff systems where step size adaptability is beneficial.


# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    k= - 1
    dydx = k * y
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 1
# step size
h = 0.2
# ------------------------------------------------------

# ------------------------------------------------------
# Fourth Order Runge-Kutta method

# number of steps
n_step = math.ceil(x_final / h)

# Definition of arrays to store the solution
y_rk = np.zeros(n_step + 1)
x_rk = np.zeros(n_step + 1)

# Initialize the first element of solution arrays
# with the initial condition
y_rk[0] = y0
x_rk[0] = x0

# Populate the x array
for i in range(n_step):
    x_rk[i + 1] = x_rk[i] + h

# Apply RK method n_step times
for i in range(n_step):
    # Compute the four slopes using the RK4 method

    # Step 1
    x_dummy = x_rk[i]
    y_dummy = y_rk[i]
    k1 = model(y_dummy, x_dummy)

    # Step 2
    x_dummy = x_rk[i] + h / 2
    y_dummy = y_rk[i] + k1 * h / 2
    k2 = model(y_dummy, x_dummy)

    # Step 3
    x_dummy = x_rk[i] + h / 2
    y_dummy = y_rk[i] + k2 * h / 2
    k3 = model(y_dummy, x_dummy)

    # Step 4
    x_dummy = x_rk[i] + h
    y_dummy = y_rk[i] + k3 * h
    k4 = model(y_dummy, x_dummy)

    # Compute the slope as a weighted average of the four slopes
    slope = 1 / 6 * k1 + 2 / 6 * k2 + 2 / 6 * k3 + 1 / 6 * k4

    # Use the RK4 method to update the solution
    y_rk[i + 1] = y_rk[i] + h * slope
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
    y_exact[i] = y0 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# print results on screen
print ('Solution: step x y-eul y-exact error%')
for i in range(n_step+1):
    print(i,x_rk[i],y_rk[i], y0 * math.exp(-x_rk[i]),
            (y_rk[i]- y0 * math.exp(-x_rk[i]))/ 
            (y0 * math.exp(-x_rk[i])) * 100)
# ------------------------------------------------------

# # ------------------------------------------------------
# # print results in a text file (for later use if needed)
# file_name= 'output_h' + str(h) + '.dat'
# f_io = open(file_name,'w')
# for i in range(n_step+1):
#     s1 = str(i)
#     s2 = str(x_rk[i])
#     s3 = str(y_rk[i])
#     s4 = s1 + ' ' + s2 + ' ' + s3
#     f_io.write(s4 + '\n')
# f_io.close()
# # ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.plot(x_rk, y_rk , 'b.-',x_exact, y_exact , 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------


