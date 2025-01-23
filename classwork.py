import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#
# def f1(x, y):
#     return x * y
#
#
# def f2(x, y):
#     return x**2 + y**2
#
#
# def f3(x, y):
#     return np.sin(3*x)*y
#
# x = np.linspace(-3, 3, 100)
# y = np.linspace(-3, 3, 100)
#
# x, y = np.meshgrid(x, y)
#
# fig, axs = plt.subplots(1, 3, figsize=(15, 5), subplot_kw={"projection": "3d"})
# z1 = f1(x, y)
# axs[0].plot_surface(x, y, z1, cmap='viridis')
# axs[0].set_title('f(x, y) = x * y')
#
# z2 = f2(x, y)
# axs[1].plot_surface(x, y, z2, cmap='viridis')
# axs[1].set_title('f(x, y) = x^2 + y^2')
#
# z3 = f3(x, y)
# axs[2].plot_surface(x, y, z3, cmap='viridis')
# axs[2].set_title('f(x, y) = sin(3x) * y')
#
# plt.show()

# def bar_chart(x, y):
#     plt.bar(x, y)
#     plt.title('Bar Chart')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#
# value_for_bars = np.loadtxt('values_for_bars.csv', delimiter=',')
# unique_values, counts = np.unique(value_for_bars, return_counts=True)
#
# plt.figure(figsize=(10, 6))
# plt.bar(unique_values, counts, color="skyblue", edgecolor="black")
# plt.title("Occurrences of Each Integer Value", fontsize=16)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Count", fontsize=14)
# plt.xticks(unique_values, rotation=45)
# plt.grid(axis="y", linestyle="--", alpha=0.7)
# plt.tight_layout()
#
# plt.show()

values = np.loadtxt('values_for_hist.csv', delimiter=',')
plt.figure(figsize=(10, 6))
plt.hist(values, bins=10, edgecolor="black")
plt.title("Histogram of Values", fontsize=16)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()