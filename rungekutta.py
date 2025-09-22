# Claire O'Connor, Amelia Abruscato & Shreyan Goswami
# Runge Kutta
import numpy as np

def k_2(yaux, t, k_1, steps):
    for i in steps:
        yaux[i] = y[i]+h * k_1[i]/2
    return func(yaux, t+h/2)

def y_next(y_prev, k_1, k_2):
    return y_prev + (k_1 + k_2)/6

def y(k_1, k_2, steps):
    for step in steps:
        y[i] = y[i] + step*(k_1[i] + 2*k_2[i])/6
    return y

def Runge(y, t, total_t, step):
    steps = total_t / step
    k_1 = func(yaux, t)
    k_2 = k_2(yaux, t + step/2, k_1, steps)
    return y(k_1, k_2, steps)
    
    
    
