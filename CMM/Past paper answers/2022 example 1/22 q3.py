import math
import matplotlib.pyplot as plt

def iterative_equation(x0, num_iterations):
    x_values = [x0]
    
    for _ in range(num_iterations):
        x_next = 1 / (math.sin(x_values[-1]) + 1/4)
        x_values.append(x_next)
    
    return x_values

# Example usage:
initial_value = 0.5
iterations = 10

result = iterative_equation(initial_value, iterations)

# Plotting
plt.plot(result, marker='o', linestyle='-')
plt.xlabel('Iteration')
plt.ylabel('x_n')
plt.title('Iterative Equation: x_{n+1} = 1/(sin(x_n) + 1/4)')
plt.show()
