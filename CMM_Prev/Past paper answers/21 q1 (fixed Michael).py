# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:51:27 2023

@author: s2192747
"""

from scipy import optimize



cm = 12
sm = 1500
def f(w):
    
    
    return w**4 + 2*cm*w**3 + 3*sm*w**2 + cm*sm*w+sm*2

#first derivative
def dfdw(w):
    return 4*(w**3 + 18*w**2 +2250*w + 4500)


#second derivative
def dfdfdw(w):
    return 4*(3*w**2+36*w+2250)



#scipy.optimize.newton used below. 

#a first guess is given for both roots by passing to x0, these guesses have to complex
#as the roots are complex

#the guesses were found by graphing the function, I used wolfram alpha as it was easiest

#the high tolerance (tol) is given as this is what the documentation reccommends for complex roots lol

root1 = optimize.newton(f, x0=complex(-1, 20), fprime=dfdw, tol = 20 , maxiter = 1000000, fprime2= dfdfdw)


root2 = optimize.newton(f, x0=complex(-11, 60), fprime=dfdw, tol = 20 , maxiter = 1000000, fprime2= dfdfdw)

#pretend j is i in the outputs lol. also, technically there are four roots, but the other two are just these roots with the complex part's sign inverted
#so w_i is just the absolute value of the given imaginary part of the root

print(root1)
print(root2)