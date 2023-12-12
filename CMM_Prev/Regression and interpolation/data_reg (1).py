#This code first visualizes the given data using a scatter plot.
# Then, it performs linear regression using manual calculations and NumPy functions.
# The results are plotted alongside the original data, and the calculated
# slope and intercept values are displayed.

import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([0., 0.06666667, 0.13333333, 0.2, 0.26666667, 0.33333333,
              0.4, 0.46666667, 0.53333333, 0.6, 0.66666667, 0.73333333,
              0.8, 0.86666667, 0.93333333, 1.])

y = np.array([2.17312991, 2.19988829, 2.33988149, 2.33940595, 2.41968027, 2.99955891,
              3.04855788, 3.86631749, 3.66009775, 4.42305111, 4.22747852, 4.11717969,
              3.87539822, 4.53121841, 5.52211102, 5.30792203])

# Visualize the data using a scatter plot
plt.scatter(x, y, label='Data Points')
plt.title('Scatter Plot of Given Data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()



# Linear regression using manual calculation

""""
Data: x and y arrays represent the input and output data points.
Calculate Mean: Calculate the mean of x and y using np.mean().
Calculate Slope (m): Use the formula to calculate the slope of the line.
Calculate Y-Intercept (b): Use the formula to calculate the y-intercept.
Linear Regression Equation: Combine slope and y-intercept to form the linear regression equation.
"""

n = len(x)
xy_sum = np.sum(x * y)
x_sum = np.sum(x)
y_sum = np.sum(y)
x_squared_sum = np.sum(x**2)

# Calculate slope (m) and intercept (c) using the formulas from lectures
m = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
c = (y_sum - m * x_sum) / n

# Create the regression line
regression_line_manual = m * x + c

# Plot the data points and the regression line
plt.scatter(x, y, label='Data Points')
plt.plot(x, regression_line_manual, label='Manual Regression Line', color='red')
plt.title('Linear Regression (Manual Calculation)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Display the calculated slope and intercept
print(f"Manual Calculation: Slope (m) = {m}, Intercept (c) = {c}")




# Linear regression using NumPy functions

"""""

# Polynomial fitting using polyfit
degree = 1  # Degree of the polynomial (linear regression)
coefficients = np.polyfit(x, y, degree)
# polyfit returns coefficients for the polynomial fit in decreasing order (highest degree first)

# Create a polynomial object using poly1d
poly = np.poly1d(coefficients)
# poly is a polynomial object that can be used for various operations

# Evaluate the polynomial at specific points
y_fit = poly(x)
# y_fit contains the y-values of the fitted polynomial for each corresponding x-value

"""

coefficients = np.polyfit(x, y, 1)
m_np, c_np = coefficients

# Create the regression line using NumPy poly1d
regression_line_np = np.poly1d(coefficients)


# Plot the original data and the fitted polynomial
plt.scatter(x, y, label='Original Data')
plt.plot(x, y_fit, label=f'Fitted Polynomial (Degree {degree})', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
# Visualization of the original data and the fitted polynomial


# Plot the data points and the regression line
plt.scatter(x, y, label='Data Points')
plt.plot(x, regression_line_np(x), label='NumPy Regression Line', color='green')
plt.title('Linear Regression (NumPy Functions)')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Display the calculated slope and intercept using NumPy functions
print(f"NumPy Functions: Slope (m) = {m_np}, Intercept (c) = {c_np}")

