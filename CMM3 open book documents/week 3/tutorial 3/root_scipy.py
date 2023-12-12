from scipy import optimize

# Definition of equation f(x)=0
# We want to find the roots of f(x)
def f(x):
    return x**2 + 4*x - 12

# First root
solution = optimize.newton(f, -10)
print(solution)

# Second root
solution = optimize.newton(f, 1.5)
print(solution)
