def bisection(f,a,b,N):
    # Check if a and b bound a root
    if f(a)*f(b) >= 0:
       print("a and b do not bound a root")
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

# we solve equation f(x)=0
f = lambda x: x**2 + 4*x - 12 
# first root
approx_phi = bisection(f,-10,-3,5) 
print(approx_phi)
# second root
approx_phi = bisection(f,0,10,5) 
print(approx_phi)
