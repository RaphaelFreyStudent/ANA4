import numpy as np

import matplotlib.pyplot as plt

y, x = np.mgrid[-5:5:30j, -5:5:30j]
u = 1
v = y**2 + 1

fig, ax = plt.subplots()
ax.quiver(x, y, u, v)

ax.axis([-5, 5, -5, 5])
plt.show()