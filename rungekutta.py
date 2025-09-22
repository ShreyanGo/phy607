# Claire O'Connor, Amelia Abruscato & Shreyan Goswami
# Runge Kutta
import numpy as np

def k_2(y, t, k_1, n):
    yaux = np.zeros(n)
    for i in range(yaux.size):
        yaux[i] = y[i]+h * k_1[i]/2
    return func(yaux, t+h/2)

def y(k_1, k_2, n):
    for i in :
        y[i] = y[i] + step*(k_1[i] + 2*k_2[i])/6
    return y

# y = current y values
# t = current time
# step = step_size
# n = number of 1st order eq (for SHM this is 2)
def RungeKutta(y, t, step, n = 2):
    yaux = np.zeros(n) # auxilary array
    k1 = func(y, t)
    k2 = func(y, t + step/2, k1, n)
    return y(k1, k2, n)
    
def func(y, t):
    f = []
    f[0] = y[1]
    f[1] = -(g/l)*np.sin(y[0])
    return f

### test
def main_():
    
