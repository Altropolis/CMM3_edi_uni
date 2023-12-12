# The original implementation utilizes the False Position Method (FPM), also known as the Regula Falsi method, for solving equations.
# FPM is a numerical technique for root finding that combines aspects of linear interpolation and bisection.
# One of the key strengths of FPM is its ability to converge reasonably quickly, especially when dealing with continuous
# functions that exhibit moderate curvature. It is particularly useful in scenarios where the function behaves approximately
# linearly in the vicinity of the root, allowing FPM to converge faster than some other methods. The method is reliable and
# generally stable, providing a good balance between simplicity and efficiency. FPM is advantageous when an initial interval is
# known where the function changes sign, and it can be a suitable choice for a wide range of continuous functions. While other methods,
# such as Newton's method, may offer faster convergence for certain functions, FPM's simplicity and robustness
# make it a valuable tool in various root-finding applications.



# Python3 implementation of False Position
# Method for solving equations

# Set a maximum number of iterations to avoid potential infinite loops
MAX_ITER = 1000000

# An example function whose solution
# is determined using False Position Method.
# The function is x^2 + 4x - 19
def func(x):
    return (x**2 + 4*x - 19)

# Prints root of func(x) in interval [a, b]
def regulaFalsi(a, b):
    # Check if the initial assumptions about 'a' and 'b' are correct
    if func(a) * func(b) >= 0:
        print("You have not assumed right 'a' and 'b'")
        return -1

    # Initialize result variable
    c = a

    # Perform iterations to approximate the root
    for i in range(MAX_ITER):
        # Find the point that touches the x-axis using linear interpolation
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))

        # Check if the above found point is the root
        if func(c) == 0:
            break

        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    # Print the approximate root and the number of iterations
    print("The value of the root is: ", '%.4f' % c)
    print("Number of iterations:", i)

# Driver code to test the regulaFalsi function
# Initial values assumed
a = -6
b = 6
regulaFalsi(a, b)

# This code is contributed by "Sharad_Bhardwaj".
