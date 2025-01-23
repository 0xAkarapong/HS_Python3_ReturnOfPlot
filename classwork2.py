import numpy as np
import matplotlib.pyplot as plt

points = np.loadtxt('points.csv', delimiter=',')
distances = np.loadtxt('distances.csv', delimiter=',')

x = points[:, 0]
y = points[:, 1]

scatter = plt.scatter(x, y, c=distances, cmap='viridis')
plt.colorbar(scatter, label='Distance')
plt.title('Scatter Plot of Points by Distance')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
