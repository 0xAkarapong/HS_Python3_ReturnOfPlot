import matplotlib.pyplot as plt
import numpy as np


def f1(x):
    return x ** 2


def f2(x):
    return x * np.sin(2 * x)


def f3(x):
    return np.arctan(x)


x = np.array(range(10))
plt.plot(f1(x), label='x^2', color='green')
plt.plot(f2(x), label='x * sin(2x)', color='red')
plt.plot(f3(x), label='arctan(x)', color='blue')

plt.title('Functions Visualization')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()