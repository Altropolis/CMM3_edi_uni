# importing modules
import numpy as np
import random
import math
import matplotlib.pyplot as plt

x = np.array([0.    ,     0.06666667, 0.13333333, 0.2   ,     0.26666667, 0.33333333,
     0.4   ,     0.46666667, 0.53333333, 0.6   ,     0.66666667, 0.73333333,
     0.8   ,     0.86666667, 0.93333333, 1.    ,    ])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
     3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
     3.87539822, 4.53121841, 5.52211102, 5.30792203])

x_y = x * y


plt.plot(x, y)

n = len(x)

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_y = np.sum(x * y)
sum_x2 = np.sum(x**2)
y_ = sum_y / n
x_ = sum_x / n


a_1 = (n*sum_x_y - sum_x*sum_y)/(n*sum_x2 - (sum_x)**2)
a_0 = y_ - a_1 * x_

#now we have the coefficients for the linear regression, we can plot the linear regression model on the same graph

def lin_reg(a_0, a_1, x):
    return a_0 + a_1 * x

plt.plot(x, lin_reg(a_0, a_1, x))

plt.show
