# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 12:52:14 2023

@author: s2086913
"""


import numpy as np
import math



def sum(n):
    x=0
    pi_tru = math.pi
    for p in range(1,n):
        x = x + (1/(p*p))
        result = np.sqrt(6*x)
    print(result)
    true_err = ((pi_tru - result)/pi_tru)*100
    print(true_err)
    return
    

sum10 = sum(10)
sum100 = sum(100)
sum1000 = sum(1000)