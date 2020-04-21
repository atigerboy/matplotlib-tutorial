import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,10, 100)

plt.plot(x, x, label="linear")
plt.legend()#show label and line mode in left top
plt.show()