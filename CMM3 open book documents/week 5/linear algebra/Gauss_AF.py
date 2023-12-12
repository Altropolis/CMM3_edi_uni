# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:13:01 2020

@author: A. Fragkou & E. McCarthy
"""

import numpy as np


#A is the left hand side of the equation. So the coefficients for each variable, for each equation. b is the right hand side,
#so it is the constant values the equations on the left hand side are equal to.
def linearsolver(A,b):
    
    #n is the number of individual arrays (one array for each equation, containing all the coefficients for that equation).
    n = len(A)
    #Initialise solution vector as an empty array, with same number of 0s as there are equations
    x = np.zeros(n)

    #Join A and use concatenate to form an augmented coefficient matrix.
    #b.T is just the transpose of the b matrix, so that it is vertical, rather than horizontal
    M = np.concatenate((A,b.T), axis=1)
    
    for k in range(n):
        for i in range(k,n):
            #M[i][k] is row i, column k
            if abs(M[i][k]) > abs(M[k][k]):
                M[[k,i]] = M[[i,k]]
            else:
                pass
                for j in range(k+1,n):
                    q = M[j][k] / M[k][k]
                    for m in range(n+1):
                        M[j][m] +=  -q * M[k][m]

    #Python starts indexing with 0, so the last element is n-1
    x[n-1] =M[n-1][n]/M[n-1][n-1]

    #We need to start at n-2, because of Python indexing
    for i in range (n-2,-1,-1):
        z = M[i][n]
        for j in range(i+1,n):
            z = z  - M[i][j]*x[j]
        x[i] = z/M[i][i]

    return x

#Initialise the matrices to be solved.
#A=np.array([[10., 15., 25],[4., 5., 6], [25, 3, 8]])
#b=np.array([[34., 25., 15]])
#print(linearsolver(A,b))

A=np.array([[70., 1., 0],[60., -1., 1.], [40, 0, -1]])
b=np.array([[636.7, 518.6, 307.4]])
print(linearsolver(A,b))

