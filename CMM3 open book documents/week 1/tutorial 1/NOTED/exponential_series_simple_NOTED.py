import math

# Set the values of x and n
x = 0.5
n = 5

# Get the exact value using the intrinsic python function for e raised to the power of x
ex_v = math.e**0.5

# Initialize the sum variable
e_to_x = 0

# Perform the iteration n times (from i=0 to i=n-1)
for i in range(n):
    # Update the sum using the Taylor series expansion formula for e^x
    e_to_x = e_to_x + x**i/math.factorial(i)

    # Print the current iteration, the updated sum, and the relative error
    print(i, e_to_x, (e_to_x - ex_v) / ex_v)

# Compute the true relative error
true_rel_error = (e_to_x - ex_v) / ex_v

# Print the final numerical result, the exact value, and the true relative error
print('numerical result', e_to_x)
print('exact value', ex_v)
print('true relative error', true_rel_error)
