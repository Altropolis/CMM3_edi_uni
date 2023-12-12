'''
Same as the simps short, but uses np.vectorise for calculations
'''



import numpy as np

import math

def simps(a,b,N):
    
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")
    dx = (b-a)/N
    expint = np.vectorize(math.exp)
    x = np.linspace(a,b,N+1)
    xint = x.astype(int)
    y = expint(-xint**2)
    S = dx/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2])
    print(S)
    return S


solution = simps(0,10,24)
print(solution)





'''
import numpy as np

def simps_38(f, a, b, N=50):
    # 3/8 Simpson's Rule implementation
    # Advantages:
    # 1. Specific Coefficients: The 3/8 rule uses coefficients (1, 3, 3, 1) for subinterval
    # contributions, improving accuracy for certain functions.
    
    # 2. Accuracy for Smooth Functions: It tends to provide more accurate results 
    # for functions with moderate smoothness.
    
    # Disadvantages:
    # 1. Less Versatility: The 3/8 rule is specialized and may not be as versatile 
    # for functions where its specific coefficients are not advantageous.
    
    if N % 3 != 0:
        raise ValueError("N must be a multiple of 3 for 3/8 Simpson's rule.")
    
    # Calculate the step size
    dx = (b - a) / N
    
    # Generate an array of x-values
    x = np.linspace(a, b, N + 1)
    
    # Evaluate the function at each x-value to get y-values
    y = f(x)
    
    # Apply 3/8 Simpson's rule formula to calculate the approximate integral
    S_38 = 3 * dx / 8 * np.sum(y[0:-1:3] + 3 * y[1::3] + 3 * y[2::3] + y[3::3])
    
    # Print the result
    print("3/8 Simpson's Rule Result:", S_38)
    
    # Return the approximate integral
    return S_38

def simps_general(f, a, b, N=50):
    # General Simpson's Rule implementation
    # Advantages:
    # 1. Versatility: The general rule is versatile and can handle any 
    # function without specific coefficients.
    # 2. Ease of Use: It is user-friendly and straightforward, making it 
    # convenient for quick integration tasks.
    
    # Disadvantages:
    # 1. Lower Specificity: The general rule may be less accurate for
    # functions that benefit from higher-order approximations.
    
    # Check if N is even (required for Simpson's rule)
    if N % 2 == 1:
        raise ValueError("N must be an even integer.")

    # Calculate the step size
    dx = (b - a) / N

    # Generate an array of x-values
    x = np.linspace(a, b, N + 1)

    # Evaluate the function at each x-value to get y-values
    y = f(x)

    # Apply Simpson's rule formula to calculate the approximate integral
    S_general = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])

    # Print the result
    print("General Simpson's Rule Result:", S_general)

    # Return the approximate integral
    return S_general

# Define the function to be integrated (exp(x**-2))
f = lambda x: np.exp(x ** -2)

# Call both functions with the given function, integration limits (1 to 2), and number of intervals (24)
solution_38 = simps_38(f, 1, 2, 24)
solution_general = simps_general(f, 1, 2, 24)
'''