# Purpose of the Code:
# The code provides a function for performing synthetic division on polynomials,
# a technique used to divide one polynomial by another. Specifically, it divides
# the dividend polynomial by the divisor polynomial and returns the quotient
# and remainder. This is useful in polynomial arithmetic and finding roots.

# When to Use:
# Use this code when you need to divide polynomials efficiently. Synthetic
# division is particularly helpful in polynomial factorization, root finding,
# and solving polynomial equations. It simplifies the process of polynomial
# division, making it a valuable tool in algebraic computations.

def extended_synthetic_division(dividend, divisor):
    # Copy the dividend to avoid modifying the original list
    out = list(dividend)

    # Get the first coefficient of the divisor
    normalizer = divisor[0]

    # Loop to perform synthetic division
    for i in range(len(dividend) - (len(divisor) - 1)):
        # Normalize the current coefficient of the dividend
        out[i] /= normalizer
        coef = out[i]

        if coef != 0:
            # Update subsequent coefficients using the divisor
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef

    # Determine the position to separate quotient and remainder
    separator = -(len(divisor) - 1)

    # Return a tuple containing quotient and remainder
    return out[:separator], out[separator:]

if __name__ == '__main__':
    print("POLYNOMIAL SYNTHETIC DIVISION")

    # Example polynomials
    N = [1, -2, -3, 5, 1]
    D = [1, -1.5]

    print("  %s / %s =" % (N, D), )

    # Call the extended_synthetic_division function and print the result
    print(" %s remainder %s" % extended_synthetic_division(N, D))
