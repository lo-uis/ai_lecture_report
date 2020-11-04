import numpy as np



x = np.array([1,2,3,4])
y = np.array([2,4,5,7])

def reg1dim(x, y):
    n = len(x)
    a = ((np.dot(x, y)- y.sum() * x.sum()/n)/
        ((x ** 2).sum() - x.sum()**2 / n))
    b = (y.sum() - a * x.sum())/n
    return a, b

a, b = reg1dim(x, y)
print("a:",a)
print("b:",b)
