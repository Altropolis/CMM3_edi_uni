# Python3 implementation of Bisection 
# Method for solving equations

# Maximum number of iterations to avoid infinite loops
MAX_ITER = 1000000

# An example function whose solution 
# is determined using Bisection Method.  
# The function is x^3 - x^2 + 2 
def func(x): 
    return (x**2 + 4*x - 19)

# Prints the root of func(x) in the interval [a, b]
def regulaFalsi(a, b): 
    # Check if the initial values of 'a' and 'b' are valid
    if func(a) * func(b) >= 0: 
        print("You have not assumed right 'a' and 'b'")
        return -1
    
    # Initialize the result variable with 'a'
    c = a

    # Iterate using a loop for a maximum number of iterations
    for i in range(MAX_ITER): 
        # Find the point that touches the x-axis using the False Position formula
        c = (a * 0.5 * func(b) - b * func(a)) / (0.5 * func(b) - func(a))
          
        # Check if the above found point is a root
        if func(c) == 0: 
            break
          
        # Decide the side to repeat the steps 
        elif func(c) * func(a) < 0: 
            b = c 
        else: 
            a = c 
    
    # Print the final root and the number of iterations
    print("The value of the root is: ", '%.4f' % c) 
    print("Number of iterations:", i)

# Driver code to test the above function 
# Initial values assumed 
a = -6
b = 6
regulaFalsi(a, b)
