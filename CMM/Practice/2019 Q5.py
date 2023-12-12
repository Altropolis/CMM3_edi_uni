import numpy as np
from scipy.optimize import minimize
def objective(X):
    th1,th2,th3 = X
    return -W1*L1*np.sin(th1) - W2*(L1*np.sin(th1)+L2*np.sin(th2))


# Define the equality constraint function with a Lagrange multiplier (lambda)
def eq(X):
    th1,th2,th3 = X
    # Define the equality constraint 2x - y + z = 3
    return L1*np.cos(th1)+L2*np.cos(th2)+L3*np.cos(th3)-B, L1*np.sin(th1)+L2*np.sin(th2)+L3*np.sin(th3)-H
L1 = 1.2; L2 = 1.5; L3 = 1.0; B = 3.5; H = 0; W1 = 20; W2 = 30

# Use the minimize function from SciPy to find the solution
# The optimization problem includes the objective function and the equality constraint
# The initial guess for optimization is [1, 4, 5]
sol = minimize(objective, [0,0,0], constraints={'type': 'eq', 'fun': eq})

# Print the optimization result
print(np.degrees(sol.x))

