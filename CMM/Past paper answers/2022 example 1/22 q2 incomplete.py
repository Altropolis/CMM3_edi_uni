
# This script demonstrates the application of the Euler method to solve a simple ordinary differential equation (ODE).
# The ODE is dy/dx = -y, and the initial condition is y(0) = 1.
# The script computes the numerical solution using the Euler method and compares it with the exact solution.
# Additionally, the results are printed on the screen, saved to a text file, and plotted for visualization.

# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math

# ------------------------------------------------------
# inputs

# Function that returns dy/dx
# The ODE we want to solve: dy/dx = -y
def model(y, x):
    k = -1
    dydx = k * y
    return dydx

# Initial conditions
x0 = 0
y0 = 1
# Total solution interval
x_final = 1
# Step size
h = 0.1
# ------------------------------------------------------

# ------------------------------------------------------
# Euler method

# Number of steps
n_step = math.ceil(x_final / h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step + 1)
x_eul = np.zeros(n_step + 1)

# Initialize the first element of solution arrays
# with the initial condition
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i + 1] = x_eul[i] + h

# Apply Euler method n_step times
for i in range(n_step):
    # Compute the slope using the differential equation
    slope = model(y_eul[i], x_eul[i]) 
    # Use the Euler method
    y_eul[i + 1] = y_eul[i] + h * slope  
# ------------------------------------------------------

# ------------------------------------------------------
# Super-refined sampling of the exact solution 
# n_exact linearly spaced numbers
# Only needed for plotting the reference solution

# Definition of the array to store the exact solution
n_exact = 1000
x_exact = np.linspace(0, x_final, n_exact + 1) 
y_exact = np.zeros(n_exact + 1)

# Exact values of the solution
for i in range(n_exact + 1):
    y_exact[i] = y0 * math.exp(-x_exact[i])
# ------------------------------------------------------

# ------------------------------------------------------
# Print results on the screen
print('Solution: step x y-eul y-exact error%')
for i in range(n_step + 1):
    print(i, x_eul[i], y_eul[i], y0 * math.exp(-x_eul[i]),
          (y_eul[i] - y0 * math.exp(-x_eul[i])) /
          (y0 * math.exp(-x_eul[i])) * 100)
# ------------------------------------------------------

# ------------------------------------------------------
# Print results in a text file (for later use if needed)
file_name = 'output_h' + str(h) + '.dat' 
f_io = open(file_name, 'w') 
for i in range(n_step + 1):
    s1 = str(i)
    s2 = str(x_eul[i])
    s3 = str(y_eul[i])
    s4 = s1 + ' ' + s2 + ' ' + s3
    f_io.write(s4 + '\n')
f_io.close()
# ------------------------------------------------------

# ------------------------------------------------------
# Plot results
plt.plot(x_eul, y_eul, 'b.-', x_exact, y_exact, 'r-')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
# ------------------------------------------------------
