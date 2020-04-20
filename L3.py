import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1,2,3,4],[10,20,25,30],color='lightblue',linewidth=3)
#marker ^:triangle ,.:point;,:pixel;o:circle;v:triangle_down;^:triangle_up
#s:square;8:octagon;p:pentagon;*:star;+:plus;x:x
ax.scatter([0.3,3.8,1.2,2.5],[11,25,9,26],color="darkgreen",marker="+")
ax.set_xlim(0,4.5)# x axis range,default contains all data
plt.show()