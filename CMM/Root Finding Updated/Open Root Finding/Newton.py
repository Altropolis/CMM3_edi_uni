
# Newton's method is chosen for root finding when the function exhibits rapid convergence characteristics. It is particularly effective when the
# initial guess is reasonably close to the actual root. Newton's method relies on iterative linear approximations of the function and utilizes the d
# erivative information to update the guess. This can result in faster convergence compared to some other root-finding methods, especially near the root.
# However, its success is contingent upon the function being differentiable and the initial guess being sufficiently close to the root. The algorithm
# iteratively refines the estimate using the formula x = xn - f(xn)/Df(xn), where f(x) is the target function, Df(x) is its derivative, and xn is the
# current approximation. The process continues until the error is within a specified tolerance or the maximum number of iterations is reached. While
# Newton's method is powerful, it may exhibit instability or fail to converge for certain functions, making careful consideration of the
# problem and function properties crucial.


def newton(f, Df, x0, epsilon, max_iter):
    '''Approximate solution of f(x)=0 by Newton's method.

    Parameters
    ----------
    f : function
        Function for which we are searching for a solution f(x)=0.
    Df : function
        Derivative of f(x).
    x0 : number
        Initial guess for a solution f(x)=0.
    epsilon : number
        Stopping criteria is abs(f(x)) < epsilon.
    max_iter : integer
        Maximum number of iterations of Newton's method.

    Returns
    -------
    xn : number
        Implement Newton's method: compute the linear approximation
        of f(x) at xn and find x intercept by the formula
            x = xn - f(xn)/Df(xn)
        Continue until abs(f(xn)) < epsilon and return xn.
        If Df(xn) == 0, return None. If the number of iterations
        exceeds max_iter, then return None.
    '''
    xn = x0  # Initial guess
    for n in range(0, max_iter):
        fxn = f(xn)  # Evaluate the function at the current guess
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations.')
            return xn  # Return the approximate root if the error is within tolerance

        Dfxn = Df(xn)  # Evaluate the derivative at the current guess
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None  # Return None if the derivative becomes zero

        xn = xn - fxn/Dfxn  # Update the guess using Newton's method formula

    print('Exceeded maximum iterations. No solution found.')
    return None  # Return None if the maximum number of iterations is reached without convergence


# Example usage of the newton function
f = lambda x: x**4 - x - 1
df = lambda x: 4*x**3 - 1
x0 = 1
epsilon = 0.001
max_iter = 100
solution = newton(f, df, x0, epsilon, max_iter)
print(solution)
