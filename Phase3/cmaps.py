import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
#   高度公式
    return (1-x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

n = 256
plt.figure(figsize=(8, 5), dpi=80)
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
# 定义网格
X,Y = np.meshgrid(x,y)
Z = f(X,Y)
# 等高线、cmap将每一块配置成热图，另一个参数cmap=plot.cm.cool
plt.contourf(X,Y,Z,12,alpha=0.65,cmap=plt.cm.hot)
# contour设置等高线的线
C = plt.contour(X,Y,Z,12,colors='black',linewidth=.5)
# inline:在等高线里
plt.clabel(C,inline='Ture',fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()