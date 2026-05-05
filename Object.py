import numpy as np
import random as rnd

def initialisation (m, n):
    A = np.random.randn(m,n)
    B = np.ones(m)
    B = B.reshape(m,1)
    C = np.concatenate((A, B), axis=1)
    return C

print(initialisation(4,3))