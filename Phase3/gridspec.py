import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# method1
plt.figure(figsize=(10, 6), dpi=80)

# 创建子窗口，基准窗格大小为3，3起始位置0，0，子窗口大小为3列1行

ax1 = plt.subplot2grid((3,3),(0,0),colspan=3, rowspan=1)
ax1.plot([1,2],[2,3])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2)
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0))
ax4 = plt.subplot2grid((3,3),(2,1))

plt.show()