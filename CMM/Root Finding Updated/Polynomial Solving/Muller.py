# This code implements Muller's method to find the root of a given function f(x). Muller's method
# iteratively refines the root approximation using three initial points (a, b, and c).
# The function f(x) is defined within the code. The algorithm calculates constants, updates
# the current approximation, and checks for convergence until the root is found or the maximum
# number of iterations is reached. The provided example demonstrates the usage of Muller's method
# with initial points a = 0, b = 1, and c = 2. The result is printed if a root is found within the
# maximum allowed iterations.

# Python3 Program to find the root of
# a function, f(x)
import math;

# Maximum number of iterations for Muller's method
MAX_ITERATIONS = 10000;

# Function to calculate f(x)
def f(x):
    # Taking f(x) = x^3 + 2x^2 + 10x - 20
    return (1 * pow(x, 3) + 2 * x * x +
            10 * x - 20);

def Muller(a, b, c):
    res = 0;  # Initialize the result
    i = 0;    # Initialize the iteration counter

    while (True):
        # Calculating various constants required to calculate x3
        f1 = f(a); f2 = f(b); f3 = f(c);
        d1 = f1 - f3;
        d2 = f2 - f3;
        h1 = a - c;
        h2 = b - c;
        a0 = f3;
        a1 = (((d2 * pow(h1, 2)) -
               (d1 * pow(h2, 2))) /
              ((h1 * h2) * (h1 - h2)));
        a2 = (((d1 * h2) - (d2 * h1)) /
              ((h1 * h2) * (h1 - h2)));
        x = ((-2 * a0) / (a1 +
             abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));
        y = ((-2 * a0) / (a1 -
             abs(math.sqrt(a1 * a1 - 4 * a0 * a2))));

        # Taking the root which is closer to x2
        if (x >= y):
            res = x + c;
        else:
            res = y + c;

        # Checking for resemblance of x3 with x2 till two decimal places
        m = res * 100;
        n = c * 100;
        m = math.floor(m);
        n = math.floor(n);
        if (m == n):
            break;

        # Update a, b, c for the next iteration
        a = b;
        b = c;
        c = res;

        # Check if the maximum number of iterations is reached
        if (i > MAX_ITERATIONS):
            print("Root cannot be found using",
                  "Muller's method");
            break;

        i += 1;

    # Print the result if it's found within the maximum iterations
    if (i <= MAX_ITERATIONS):
        print("The value of the root is",
              round(res, 4));

# Driver Code
a = 0;
b = 1;
c = 2;
Muller(a, b, c);

# This code is contributed by mits
