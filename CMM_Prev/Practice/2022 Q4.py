import numpy as np
import matplotlib.pyplot as plt
import math
step = 1000
t = np.linspace(0,100,step)
A0,b,phi,m,w0 = 0.05,0.1,0,1,5
w = np.sqrt(w0**2-(b/2*m)**2)
x = A0 * np.exp(-t * (b / (2 * m))) * np.cos(w * t + phi)
plt.plot(t,x)
plt.show()
amp = 0.01*0.05
T=w/(2*np.pi)
Tspan = math.ceil(T*step)
i = False
k = 0
Check = []
while i == False:
    Check = []
    for j in range(Tspan + k):
        if abs(x[j]) > amp:
            Check.append(False)
        else:
            Check.append(True)
    if all(p==True for p in Check):
        i = True

    k += 1
print(k)