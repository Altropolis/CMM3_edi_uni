"""""

The code uses the solve_ivp function from the scipy.integrate module to numerically solve
a system of ordinary differential equations (ODEs). This function is particularly useful
when dealing with complex systems where analytical solutions are challenging or impossible
to find. In this specific example, the ODE system is defined by the model function, representing
two differential equations. The initial conditions, total solution interval, and other parameters
are specified, and then solve_ivp is employed to calculate the solution.

The advantage of solve_ivp lies in its ability to handle a variety of ODE problems efficiently, providing
adaptive step size control and a choice of integration methods. This flexibility makes it suitable for
a wide range of applications. The code then plots the results and saves them to a text file for further
analysis or visualization. Overall, solve_ivp simplifies the process of solving
complex ODE systems by automating the numerical integration and offering a versatile tool
for various scientific and engineering simulations.
"""


# importing modules
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import solve_ivp

# ------------------------------------------------------
# functions that returns dy/dx
# i.e. the equation we want to solve:
# dy_j/dx = f_j(x,y_j) (j=[1,2] in this case)
def model(x,y):
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]
    f_1 = 10*(y_2-y_1)
    f_2 = 28*y_1-y_2-y_1*y_3
    f_3 = -8/3*y_3 + y_1*y_2
    return [f_1 , f_2, f_3]
# ------------------------------------------------------

# ------------------------------------------------------
# initial conditions
x0 = 0
y0_1 = 5
y0_2 = 5
y0_3 = 5
# total solution interval
x_final = 30
# step size not needed here. The solver solve_ivp  will take care of finding the appropriate step
# ------------------------------------------------------

# ------------------------------------------------------
# Apply solve_ivp method
t_eval = np.linspace(0,x_final,5000)
y = solve_ivp(model, [0 , x_final] ,[y0_1 , y0_2, y0_3], t_eval=t_eval)
# ------------------------------------------------------

# ------------------------------------------------------
# plot results
plt.figure(1)
plt.plot(y.t,y.y[0,:] , 'b.-',y.t,y.y[1,:] , 'r-', y.t,y.y[2,:] , 'g-')
plt.xlabel('x')
plt.ylabel('y_1(x), y_2(x), y_3(x)')

plt.figure(2)
plt.plot(y.y[0,:],y.y[1,:])
plt.xlabel('y_1')
plt.ylabel('y_2')

plt.show()
# ------------------------------------------------------

# ------------------------------------------------------
# # print results in a text file (for later use if needed)
# file_name= 'output.dat'
# f_io = open(file_name,'w')
# n_step = len(y.t)
# for i in range(n_step):
#     s1 = str(i)
#     s2 = str(y.t[i])
#     s3 = str(y.y[0,i])
#     s4 = str(y.y[1,i])
#     s_tot = s1 + ' ' + s2 + ' ' + s3  + ' ' + s4
#     f_io.write(s_tot + '\n')
# f_io.close()
# # ------------------------------------------------------
#
