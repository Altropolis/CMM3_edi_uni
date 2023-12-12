import numpy as np

def poly_iter(A, t):
    # compute q(x) = p(x)/(x-t) and residual r
    # array A contains coefficients of p(x) 
    
    #n is the order of the polynomial, which is one less than the number of coefficients in the polynomial.
    n = len(A)-1
    # q: array of integers to store coefficients of q(x)
    q=np.zeros(n,dtype=np.int8)
    #r is the remainder after the division
    r = A[n]
    #range from n back down to 0
    for a in reversed(range(n)):
        s=A[a]
        q[a]=r
        r = s + r * t
    print('----------------------------------------')
    print('Coefficients a0, a1, a2, ..., an')
    print('of quotient a0+a1*x+a2*x^2+...an*x^n:') 
    print(q)
    print('----------------------------------------')
    print('Residual:')
    print(r)
    print('----------------------------------------')
    return []

A = np.array([ -24, 2, 1])
t = 4

#A = np.array([ -42, 0, -12 ,1])
#t=3

poly_iter(A,t)
