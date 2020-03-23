#qesolution calculates the roots for the equation x^2-2bx-c=0 for b>0, c>0

import numpy as np

def qesolution(b, c):
    n = 4.0 * (b**2.0 + c)
    r1 = (2.0 * b - np.sqrt(n))/2.0
    r2 = (2.0 * b + np.sqrt(n))/2.0
    return (r1,r2)



print (qesolution(10,12))