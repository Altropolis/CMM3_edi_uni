# Function to perform Inverse Quadratic Interpolation to find the root of a given function
def inverse_quadratic_interpolation(f, x0, x1, x2, max_iter=20000000, tolerance=1e-5):
    # Initialize the number of steps taken
    steps_taken = 0
    
    # Continue iterating until the maximum number of iterations is reached or the difference between last and new guesses is small
    while steps_taken < max_iter and abs(x1 - x0) > tolerance:  # last guess and new guess are very close
        # Evaluate the function at the current guesses
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)
        
        # Calculate interpolation coefficients L0, L1, and L2
        L0 = (x0 * fx1 * fx2) / ((fx0 - fx1) * (fx0 - fx2))
        L1 = (x1 * fx0 * fx2) / ((fx1 - fx0) * (fx1 - fx2))
        L2 = (x2 * fx1 * fx0) / ((fx2 - fx0) * (fx2 - fx1))
        
        # Calculate the new guess using the interpolation coefficients
        new = L0 + L1 + L2
        
        # Update the guesses for the next iteration
        x0, x1, x2 = new, x0, x1
        
        # Increment the number of steps taken
        steps_taken += 1
    
    # Return the final guess and the number of steps taken
    return x0, steps_taken

# Define a test function (a cubic function)
f = lambda x: x**3 + 2*x**2 + 4*x + 5

# Use the Inverse Quadratic Interpolation method to find the root with initial guesses of 4.3, 4.4, and 4.5
root, steps = inverse_quadratic_interpolation(f, 4.3, 4.4, 4.5)

# Print the results
print("Root is:", root)
print("Steps taken:", steps)
