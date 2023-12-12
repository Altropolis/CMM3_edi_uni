#1

import numpy as np
import scipy.integrate import quad
import matplotlib.pyplot as plt
cm = 12
sm = 1500
# def f(w,cm,sm):
#     w**4+2*cm*w**3+3*sm*w**2+cm*sm*w+sm**2
# w = np.linspace(0,5,100)
# y = f(w,cm,sm)
# # xest,yest = root, f(root)
# # plt.plot(xest, yest, marker="o", markersize=5)
# plt.plot(w,y)
# plt.show()

w = np.roots([1, 2*cm, 3*sm, cm*sm, sm**2])

print(w)

#2

wr = w[2].real
wi = w[2].imag

f = lamda x: A0
