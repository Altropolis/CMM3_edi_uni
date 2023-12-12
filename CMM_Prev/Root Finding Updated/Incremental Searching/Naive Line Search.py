# This code demonstrates a naive root-finding approach using a simple line search with a fixed step size.
# The function `naive_root` takes as input a function `f`, an initial guess `x_guess`, a tolerance level,
# and a step size. It iteratively adjusts the guess based on the sign of the function value until the
# absolute value of `f(x_guess)` is within the specified tolerance. While this method is straightforward,
# it may not be efficient for all functions, especially those with complex roots or rapid changes in slope.
# Other root-finding techniques, like Newton's method or the bisection method, may be more suitable for
# certain cases. This example uses the function f(x) = x**2 - 20 to find its root, demonstrating the
# simplicity of the line search approach.


def naive_root(f, x_guess, tolerance, step_size):
    # Initialize a variable to keep track of the number of steps taken
    steps_taken = 0

    # Continue iterating until the absolute value of f(x_guess) is less than the specified tolerance
    while abs(f(x_guess)) > tolerance:
        # If f(x_guess) is positive, adjust x_guess to the left by subtracting the step_size
        if f(x_guess) > 0:
            x_guess -= step_size
        # If f(x_guess) is negative, adjust x_guess to the right by adding the step_size
        elif f(x_guess) < 0:
            x_guess += step_size
        # If f(x_guess) is exactly zero, the root has been found, and the function returns the current guess
        else:
            return x_guess

        # Increment the steps_taken counter for each iteration
        steps_taken += 1

    # Return the final x_guess and the number of steps taken
    return x_guess, steps_taken


# Define the function f(x) = x**2 - 20
f = lambda x: x ** 2 - 20

# Call the naive_root function with initial guess x_guess=4.5, tolerance=0.01, and step_size=0.001
root, steps = naive_root(f, x_guess=-4.5, tolerance=0.01, step_size=0.001)

# Print the result (root) and the number of steps taken
print("root is:", root)
print("steps taken:", steps)
