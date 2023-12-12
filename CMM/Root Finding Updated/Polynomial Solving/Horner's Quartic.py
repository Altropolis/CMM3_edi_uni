# choose Horner's method for efficiency and numerical stability, the naive approach for
# simplicity and small-degree polynomials, and the iterative approach when variable powers
# are already computed or when intermediate results are needed. Consider the specific
# requirements and characteristics of your problem to make an informed choice.

def poly_horner(A, x):
    p = A[-1]  # Initialize p with the last coefficient
    i = len(A) - 2  # Start from the second-to-last coefficient
    while i >= 0:
        p = p * x + A[i]  # Update p using the current coefficient
        i -= 1
    return p

# Function to evaluate a polynomial using the naive approach
def poly_naive(A, x):
    p = 0
    for i, a in enumerate(A):
        p += (x ** i) * a  # Update p using each coefficient and x raised to the corresponding power
    return p

# Function to evaluate a polynomial using an iterative approach
def poly_iter(A, x):
    p = 0
    xn = 1
    for a in A:
        p += xn * a  # Update p using each coefficient multiplied by the corresponding power of x
        xn *= x
    return p

# Coefficients of the polynomial: A[0] * x^n + A[1] * x^n-1 ... A[n] * x^0
A = [1, -2, -3, 5, 1]

# Value of x for evaluation
x = 0.59

# Print the results of polynomial evaluation using different methods
print(poly_horner(A, x))
print(poly_naive(A, x))
print(poly_iter(A, x))
