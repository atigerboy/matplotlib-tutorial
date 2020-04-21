import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

#ax bare basic:
#bar:vertical rectangles; barh:horizontal rectangles
#axhline:Horizontal line across axes;
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45,color="red")
ax1.axvline(0.65,color="blue")


plt.show()