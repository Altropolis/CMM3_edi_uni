# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:56:21 2023

@author: s2192747
"""

import math

def fixed_point_iteration(initial_guess, tolerance, max_iterations):
    x_n = initial_guess

    for iteration in range(max_iterations):
        x_n_plus_1 = 1 / math.sin(x_n) + 1 / 4

        # Check for convergence
        if abs(x_n_plus_1 - x_n) < tolerance:
            return x_n_plus_1, iteration + 1

        x_n = x_n_plus_1

    return None, max_iterations

def main():
    # Set initial guess, tolerance, and maximum iterations
    initial_guess = 2.0  # Choose a value within the specified domain (0 < x < 4)
    tolerance = 1e-8
    max_iterations = 1000

    # Perform fixed-point iteration
    root, iterations = fixed_point_iteration(initial_guess, tolerance, max_iterations)

    if root is not None:
        print(f"Root found: {root} (converged in {iterations} iterations)")
    else:
        print(f"Root not found within {max_iterations} iterations")

main()