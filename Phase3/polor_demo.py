import numpy as np
import matplotlib.pyplot as plt

plt.rc('grid', color='#316931', linewidth=1, linestyle='-')
plt.rc('xtick', labelsize=15)
plt.rc('ytick', labelsize=15)

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r,label=r"$r(x)=\frac{ x}{2*\pi}$")
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.legend(loc="upper right",bbox_to_anchor=(1.1,1.1))

ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()