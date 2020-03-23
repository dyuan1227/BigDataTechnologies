# Solving the quadratic function using a more numerically stable form
import math


import numpy as np

def qesolutionRevise(b,c):
    y = 4.0 * (b**2.0 + c)
    if b>0:
        r1 = (2*b + np.sqrt(y))/2
        r2 = -2*c/(2*b+np.sqrt(y))
    else:
        r1 = (2*b - np.sqrt(y))/2
        r2 = -2*c/(2*b-np.sqrt(y))
    return (r1, r2)

print (qesolutionRevise(10,12))