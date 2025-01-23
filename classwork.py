import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**2

def f2(x):
    return x * np.sin(2 * x)

def f3(x):
    return np.arctan(x)

x = np.array(range(10))
plt.plot(f1(x))
plt.plot(f2(x))
plt.plot(f3(x))
plt.show()