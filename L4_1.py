import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

ax = fig.add_axes([0,0,1,1])#111 equal 1,1,1 ：row 1, column 1, plot 1.
ax.scatter(np.linspace(0,1,5),np.linspace(0,5,5),marker=8)

plt.show()