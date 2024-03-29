# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 12:38:41 2020

@author: emc1977
"""

import numpy as np
from scipy.integrate import quad

def func(x): 
      
    return (x**2 + 4*x - 12) 
  
# Function to perform calculations 
def calculate(lower_limit, upper_limit, interval_limit ): 
      
    interval_size = (float(upper_limit - lower_limit) / interval_limit) 
    sum = func(lower_limit) + func(upper_limit); 
   
    # Calculates value till integral limit 
    for i in range(1, interval_limit ): 
        if (i % 3 == 0): 
            sum = sum + 2 * func(lower_limit + i * interval_size) 
        else: 
            sum = sum + 3 * func(lower_limit + i * interval_size) 
      
    return ((float( 3 * interval_size) / 8 ) * sum ) 
  
# driver function 
interval_limit = 1000
lower_limit = -10
upper_limit = 10
  
integral_res = calculate(lower_limit, upper_limit, interval_limit) 
  
# rounding the final answer to 6 decimal places  
def error(f, a, b, k):
    q = quad(f, -10, 10)
    true_error = abs(k)-(q[0])
    return true_error
integral_res
print(solution, error(f, -10, 10, integral_res))
# This code is contributed by Saloni. 

