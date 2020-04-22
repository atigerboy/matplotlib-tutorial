import numpy as np
import matplotlib.pyplot as plt

n =1024
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
# for color value 色彩数量值
t = np.arctan2(y,x)

plt.figure(figsize=(8, 5), dpi=80)
# 主要方程式(x,y坐标，形状，透明度)
plt.scatter(x,y,s=75,c=t,marker='+',alpha=.5)
# plt.scatter(np.arange(5),np.arange(5))
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.xticks(())
plt.yticks(())
plt.show()