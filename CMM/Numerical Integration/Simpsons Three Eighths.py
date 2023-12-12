'''' 
The 3/8 Simpson's rule is a numerical integration method that offers advantages in terms of 
accuracy and simplicity, making it a preferred choice in certain scenarios. Unlike simpler methods
 like the trapezoidal rule, the 3/8 Simpson's rule uses quadratic interpolations for each subinterval,
 providing a more accurate approximation of definite integrals. This is particularly beneficial
 when dealing with functions that exhibit moderate smoothness or oscillatory behavior. The 3/8 
 rule, with its specific coefficients (1, 3, 3, 1) for subinterval contributions, reduces error
 and converges more rapidly, leading to improved accuracy compared to other methods. While the
 method requires an even number of intervals, this condition is often manageable, especially 
 considering the performance gains in accuracy and efficiency. Overall, the 3/8 Simpson's rule 
 is a reliable choice when seeking a balance between accuracy and simplicity in numerical integration,
 especially for functions where higher-order approximations are necessary.
'''


# Importing the NumPy library for numerical operations
import numpy as np


# Function definition for the integrand (function to be integrated)
def func(x):
    return (np.exp(-x ** 2))


# Function to perform numerical integration using Simpson's 3/8 rule
def calculate(lower_limit, upper_limit, interval_limit):
    # Calculate the size of each subinterval
    interval_size = (float(upper_limit - lower_limit) / interval_limit)

    # Initialize the sum with the values at the lower and upper limits
    sum = func(lower_limit) + func(upper_limit)

    # Iterate over the subintervals and accumulate the sum based on Simpson's rule coefficients
    for i in range(1, interval_limit):
        if (i % 3 == 0):
            # For every third interval, use a coefficient of 2
            sum = sum + 2 * func(lower_limit + i * interval_size)
        else:
            # For other intervals, use a coefficient of 3
            sum = sum + 3 * func(lower_limit + i * interval_size)

            # Calculate the final result using the Simpson's 3/8 rule formula
    result = (float(3 * interval_size) / 8) * sum

    # Return the calculated result
    return result


# Driver code
interval_limit = 1000
lower_limit = 1
upper_limit = 2

# Perform numerical integration and store the result
integral_res = calculate(lower_limit, upper_limit, interval_limit)

# Print the rounded result to 6 decimal places
print(round(integral_res, 6))

# This code is contributed by Saloni.




