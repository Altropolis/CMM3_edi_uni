# This Python program demonstrates a simple optimization algorithm, specifically the
# steepest ascent method, to find a local maximum of a given objective function. The
# objective function, defined by F(x, y), represents a surface, and the program iteratively
# ascends along the steepest direction, adjusting the parameters x and y. The steepest
# ascent is determined by the partial derivatives dF/dx and dF/dy. The optimization path
# is visualized by storing the values of x, y, F(x, y), dF/dx, and dF/dy at each iteration.
# The algorithm stops when both partial derivatives are below a specified threshold,
# indicating convergence, or after a maximum number of iterations. Use cases for this
# type of optimization include finding maximum values in mathematical models, optimizing
# parameters in machine learning algorithms, and other scenarios where the objective is
# to ascend to a local maximum. It is important to note that the steepest ascent method
# may converge to a local maximum, and the effectiveness depends on the nature of the
# objective function.



# Import necessary libraries
def HOpt(F, dFx, dFy, x, y):
    import sympy as sym
    from sympy import symbols, solve
    import matplotlib.pyplot as plt

    # Define a symbolic variable hsym for optimization parameter
    hsym = symbols('hsym')

    # Initialize lists to store optimization path information
    xlist = []
    ylist = []
    flist = []
    dfxlist = []
    dfylist = []

    # Perform optimization steps (up to 10 iterations in this case)
    for i in range(10):
        # Save current values of x and y
        xold = x
        yold = y

        # Compute partial derivatives df/dx and df/dy
        dfx = dFx(x)
        dfy = dFy(y)

        # Create a function for the path to the top of the mountain
        g = F(x + dfx * hsym, y + dfy * hsym)
        hexpr = sym.diff(g, hsym)

        # Solve for the optimal step size hopt
        hsolved = solve(hexpr)
        hopt = hsolved[0]

        # Update x and y using the optimal step size
        x = xold + hopt * dfx
        y = yold + hopt * dfy

        # Evaluate the objective function F at the new (x, y)
        Fxy = F(x, y)

        # Recalculate partial derivatives df/dx and df/dy
        dfx = dFx(x)
        dfy = dFy(y)

        # Store the values for later analysis
        xlist.append(x)
        ylist.append(y)
        flist.append(Fxy)
        dfxlist.append(dfx)
        dfylist.append(dfy)

        # Check for convergence (if partial derivatives are small)
        if dfx <= 0.0001 and dfy <= 0.0001:
            break

    # Print the final values after optimization
    print(x, y, Fxy, dfx, dfy)

# Define the objective function F(x, y)
def F(x, y):
    return 2 * x * y + 2 * x - x**2 - 2 * y**2

# Define the partial derivative df/dx
def dFx(x):
    return 2 * y + 2 - 2 * x

# Define the partial derivative df/dy
def dFy(y):
    return 2 * x - 4 * y

# Initial values for x and y
x = 1.
y = 1.

# Call the optimization function and print the result
print(HOpt(F, dFx, dFy, x, y))
xx