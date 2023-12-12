

# Fixed Point Iteration Method

# The Fixed Point Iteration method is employed for root finding, providing a simple and iterative approach to approximate solutions of nonlinear equations.
# This method is particularly useful when the original equation can be rewritten in the form x = g(x), where g(x) is a continuous function.
# Fixed Point Iteration is chosen over other root-finding methods in scenarios where the function exhibits convergence behavior suitable for iterative updating
# of the initial guess. The process involves starting with an initial guess, iteratively applying the function g(x) to generate new approximations, and checking
# for convergence based on a tolerable error or a maximum number of iterations. While the method's simplicity is an advantage, its effectiveness depends on the
# characteristics of the function and the choice of the iterative function g(x). The method is more likely to succeed when the derivative of g(x) is bounded and the
# fixed point is attractive. However, it may converge slowly or fail to converge for certain functions. Users should carefully consider the nature of the problem
# and the specific properties of the function before opting for the Fixed Point Iteration method.


# Importing math to use sqrt function
import math

# Input Section
x0 = 0
e = 1e-3
N = 1000

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Fixed Point Iteration Method
# Importing math to use sqrt function
import math

def f(x):
    return x**2 + 4*x -12

# Re-writing f(x)=0 to x = g(x)
def g(x):
    return 0.25*(12-x**2)
    
# Implementing Fixed Point Iteration Method
def fixedPointIteration(x0, e, N):
    print('\n\n*** FIXED POINT ITERATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1

        step = step + 1
        
        if step > N:
            flag=0
            break
        
        condition = abs(f(x1)) > e

    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
fixedPointIteration(x0,e,N)