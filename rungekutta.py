# Claire O'Connor, Amelia Abruscato & Shreyan Goswami
# Runge Kutta
import numpy as np

def k_2(y, t, k_1, n):
    yaux = np.zeros(n)
    for i in range(yaux.size):
        yaux[i] = y[i]+h * k_1[i]/2
    return func(yaux, t+h/2)

def y_next(y, k_1, k_2, n, step):
    for i in range(n):
        y[i] = y[i] + step*(k_1[i] + 2*k_2[i])/6
    return y

# y = current y values
# t = current time
# step = step_size
# n = number of 1st order eq (for SHM this is 2)
def RungeKutta(y, t, step, mass=10, n = 2):
    yaux = np.zeros(n) # auxilary array
    k1 = func(y, t, mass)
    k2 = func(y, t + step/2, mass)
    return y_next(y, k1, k2, n, step)
    
def func(y, t, mass, k=1):
    f = [y[1]]
    f.append(-k*np.sin(y[0]))
    PE = -k*(y[0])**2
    KE = 0.5 * mass * (y[1])**2
    f.append(PE)
    f.append(KE)
    return f

    
