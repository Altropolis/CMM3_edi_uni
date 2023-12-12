# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 20:13:55 2023

@author: s2192747
"""


import math
import matplotlib.pyplot as plt

def fixed_point_iteration(initial_guess, tolerance, max_iterations):
    x_values = [initial_guess]
    x_n = initial_guess

    for iteration in range(max_iterations):
        x_n_plus_1 = 1 / math.sin(x_n) + 1 / 4

        # Check for convergence
        if abs(x_n_plus_1 - x_n) < tolerance:
            return x_values, iteration + 1

        x_n = x_n_plus_1
        x_values.append(x_n)

    return x_values, max_iterations

def main():
    # Set initial guess, tolerance, and maximum iterations
    initial_guess = 2.0  # Choose a value within the specified domain (0 < x < 4)
    tolerance = 1e-8
    max_iterations = 1000

    # Perform fixed-point iteration
    x_values, iterations = fixed_point_iteration(initial_guess, tolerance, max_iterations)

    if x_values[-1] is not None:
        print(f"Root found: {x_values[-1]} (converged in {iterations} iterations)")
    else:
        print(f"Root not found within {max_iterations} iterations")

    # Plot the function values during iteration
    plt.plot(range(len(x_values)), x_values, marker='o', linestyle='-', color='b')
    plt.xlabel('Iteration')
    plt.ylabel('x value')
    plt.title('Fixed-Point Iteration')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()