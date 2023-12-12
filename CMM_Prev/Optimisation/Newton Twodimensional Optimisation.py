# This Python program implements the Newton-Raphson optimization algorithm to find
# the minimum of a given two-dimensional objective function. The objective function,
# defined by the Function(x, y) method, represents the Rosenbrock function, a commonly
# used test problem in optimization. The algorithm utilizes the gradient (Grad) and
# Hessian matrix (Hessian) of the function to iteratively update the solution, aiming to
# converge to the minimum. The Newton-Raphson method is particularly effective for
# well-behaved, smooth functions and can converge rapidly when the initial guess is close
# to the optimal solution. It is crucial for optimization problems where analytical
# derivatives (gradient and Hessian) can be efficiently computed. The program outputs
# the optimized solution, as well as the intermediate iterates for further analysis.
# It can be employed in various optimization scenarios, such as parameter tuning, machine
# learning model training, and engineering design, where finding the optimal set of
# parameters is essential for achieving desired performance or results.



# Import necessary libraries
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')
import numpy as np


# Define the objective function
def Function(x, y):
    return (1 + x) ** 2 + 100 * (y - x ** 2) ** 2


# Define the gradient of the objective function
def Grad(x, y):
    g1 = -400 * x * y + 400 * x ** 3 + 2 * x - 2
    g2 = 200 * y - 200 * x ** 2
    return np.array([g1, g2])


# Define the Hessian matrix of the objective function
def Hessian(x, y):
    h11 = -400 * y + 1200 * x ** 2 + 2
    h12 = -400 * x
    h21 = -400 * x
    h22 = 200
    return np.array([[h11, h12], [h21, h22]])


# Implement the Newton-Raphson optimization algorithm
def Newton_Raphson_Optimize(Grad, Hess, x, y, epsilon=0.000001, nMax=200):
    # Initialization
    i = 0
    iter_x, iter_y, iter_count = np.empty(0), np.empty(0), np.empty(0)
    error = 10
    X = np.array([x, y])

    # Looping as long as error is greater than epsilon and within the maximum number of iterations
    while np.linalg.norm(error) > epsilon and i < nMax:
        i += 1
        iter_x = np.append(iter_x, x)
        iter_y = np.append(iter_y, y)
        iter_count = np.append(iter_count, i)

        # Display current solution in each iteration
        print(X)

        X_prev = X
        # Update the solution using the Newton-Raphson formula
        X = X - np.linalg.inv(Hess(x, y)) @ Grad(x, y)
        error = X - X_prev
        x, y = X[0], X[1]

    # Print the final solution
    print(X)
    return X, iter_x, iter_y, iter_count


# Execute the Newton-Raphson optimization with an initial guess of (-2, 2)
root, iter_x, iter_y, iter_count = Newton_Raphson_Optimize(Grad, Hessian, -2, 2)
