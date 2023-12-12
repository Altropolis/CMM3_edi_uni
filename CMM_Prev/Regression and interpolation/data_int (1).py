#This code first plots the given data points and then uses B-spline interpolation to
# increase the resolution to 128 points. The original data and the interpolated spline
# are plotted for comparison. The splrep function creates the B-spline representation,
# and splev evaluates the spline at high-resolution x values.


import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([0., 0.06666667, 0.13333333, 0.2, 0.26666667, 0.33333333,
              0.4, 0.46666667, 0.53333333, 0.6, 0.66666667, 0.73333333,
              0.8, 0.86666667, 0.93333333, 1.])

y = np.array([0.00000000e+00, 7.78309056e-01, 1.24040577e+00, 1.24494914e+00,
              8.90566050e-01, 4.33012702e-01, 1.12256994e-01, 4.54336928e-03,
              -4.54336928e-03, -1.12256994e-01, -4.33012702e-01, -8.90566050e-01,
              -1.24494914e+00, -1.24040577e+00, -7.78309056e-01, -4.89858720e-16])

# Plotting the original data
plt.plot(x, y, 'o-', label='Original Data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Original Data Points')
plt.legend()
plt.grid(True)
plt.show()


from scipy.interpolate import splrep, splev

# Using splrep to create B-spline representation
spl = splrep(x, y, k=3)  # k is the degree of the spline


# Increase the resolution to have 128 points
x_high_res = np.linspace(0, 1, 128)  # New points for evaluation

# Use splev to evaluate the spline on the high-resolution x values
y_interp = splev(x_high_res, spl)

# Plotting the original data and the interpolated spline
plt.plot(x, y, 'o-', label='Original Data')
plt.plot(x_high_res, y_interp, label='Interpolated Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Original Data and Interpolated Spline')
plt.legend()
plt.grid(True)
plt.show()
