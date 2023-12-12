# Function to find a root of a given function using a naive approach
def naive_root(f, x_guess, tolerance, step_size):
    # Initialize the number of steps taken
    steps_taken = 0
    
    # Continue iterating until the absolute value of f(x_guess) is less than the specified tolerance
    while abs(f(x_guess)) > tolerance:
        # Adjust the guess based on the sign of f(x_guess)
        if f(x_guess) > 0:
            x_guess -= step_size
        elif f(x_guess) < 0:
            x_guess += step_size
        else:
            # Return the current guess if f(x_guess) is exactly 0
            return x_guess
        
        # Increment the number of steps taken
        steps_taken += 1
    
    # Return the final guess and the number of steps taken
    return x_guess, steps_taken

# Define a test function (quadratic function with a root at sqrt(20))
f = lambda x: x**2 - 20

# Use the naive_root function to find the root with initial guess of 4.5, tolerance of 0.01, and step size of 0.001
root, steps = naive_root(f, x_guess=4.5, tolerance=0.01, step_size=0.001)

# Print the results
print("Root is:", root)
print("Steps taken:", steps)
