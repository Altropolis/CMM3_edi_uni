# Python3 implementation of False Position 
# Method for solving equations

# Maximum number of iterations to avoid infinite loops
MAX_ITER = 1000000

# An example function whose solution 
# is determined using False Position Method.  
# The function is x^3 - x^2 + 2
def func(x): 
    return (x**2 + 4*x - 19) 

# Function to find the root of func(x) in the interval [a, b]
def regulaFalsi(a, b): 
    # Check if the initial values of 'a' and 'b' are valid
    if func(a) * func(b) >= 0: 
        print("You have not assumed right 'a' and 'b'") 
        return -1
      
    c = a  # Initialize the result variable with 'a'
      
    for i in range(MAX_ITER): 
        # Find the point that touches the x-axis using the False Position formula
        c = (a * func(b) - b * func(a)) / (func(b) - func(a)) 
        
        # Check if the found point is the root
        if func(c) == 0: 
            break
        
        # Decide the side to repeat the steps
        elif func(c) * func(a) < 0: 
            b = c  # Update 'b' if the root is on the same side as 'a'
        else: 
            a = c  # Update 'a' if the root is on the same side as 'b'
    
    # Print the root and the number of iterations
    print("The value of the root is:", '%.4f' % c) 
    print("Number of iterations:", i)

# Driver code to test the regulaFalsi function 
# Initial values assumed 
a = -6
b = 6
regulaFalsi(a, b) 
