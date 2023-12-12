# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:08:21 2023

@author: s2192747
"""

import math

def bisection(f,a,b,N):
    
    
    
    '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.

    Parameters
    ----------
    f : function
        The function for which we are trying to approximate a solution f(x)=0.
    a,b : numbers
        The interval in which to search for a solution. The function returns
        None if f(a)*f(b) >= 0 since a solution is not guaranteed.
    N : (positive) integer
        The number of iterations to implement.

    Returns
    -------
    x_N : number
        The midpoint of the Nth interval computed by the bisection method. The
        initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
        midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
        If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
        iteration, the bisection method fails and return None.

    Examples
    --------
    f = lambda x: x**2 - x - 1
    bisection(f,1,2,25)
    1.618033990263939
    f = lambda x: (2*x - 1)*(x - 3)
    >>> bisection(f,0,1,10)
    0.5
    '''
   
#    Re = 13,743
#    D = 0.005
#    e = 0.000005
      
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return (a_n + b_n)/2

#f = lambda x: x-(1.325/(math.log((0.000005/3.7*0.005)+5.74/13,473*0.9))*2)
f = lambda x: math.cosh(x)*math.cos(x)+1
root_1 = bisection(f,1,2,25)
print(root_1)

root_2 = bisection(f, 4,5,25)
print(root_2)


m = 7850
L = 0.9
E= 200*10**9
I = 3.255*10**-11

b = root_1

f = (math.sqrt(E*I*(b*4)/(m*L*3))/(2*math.pi))


print(f)

b = root_2

f2 = (math.sqrt(E*I*(b*4)/(m*L*3))/(2*math.pi))

print(f2)