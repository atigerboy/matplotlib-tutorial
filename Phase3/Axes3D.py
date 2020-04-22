import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.figure(figsize=(10, 6), dpi=80)
# 设置三维坐标  
fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
# XY平面的网格数据 
X,Y = np.meshgrid(X,Y)
Z = np.sin(np.sqrt(X**2+Y**2))

# 画3d图rstride=row_stride行跨、cstride=column_stride列跨
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
# 等高线图,zdir以Z轴为映射方向，offset刻度值,
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
# 固定Z的范围
ax.set_zlim(-2,2)
plt.show()