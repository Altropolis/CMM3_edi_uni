import numpy as np

def pi_approximation(N):
    P = np.sqrt(6 * np.sum(1/np.arange(1, N+1)**2))
    return P

approx_pi_10 = pi_approximation(10)
approx_pi_100 = pi_approximation(100)
approx_pi_1000 = pi_approximation(1000)

Pi = np.pi

print('at N = 10 , the aproximation of Pi is ', approx_pi_10)
print('at N = 100 , the aproximation of Pi is ', approx_pi_100)
print('at N = 1000 , the aproximation of Pi is ', approx_pi_1000)


print('the exact value of Pi is ', Pi)


def error_calc(N):
    error = (Pi - pi_approximation(N))/Pi
    percentage = error * 100
    print(error, 
          percentage,'%')
    return

error_calc(10)