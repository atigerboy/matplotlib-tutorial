import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

def func(x ):
    return x**3 - 2* x**2 + 5
def deff_func(x):
    return 3*x**2 - 4*x

m1 = deff_func(2)
m2 = -1/m1
y1 = func(2)
# line 
def func_tangent_line(x):
    return y1 + m1 *( x - 2)

def func_normal_line(x):
    return y1 + m2 * ( x - 2)

x = np.linspace(-3, 3, 50)
# 定义线

plt.figure(figsize=(8,5))
# 定义轴名
plt.xlabel('x')
plt.xlabel('y')

l1, = plt.plot(x,func(x),label = 'up', color = 'g', alpha = 0.7 )
l2, = plt.plot(x,func_tangent_line(x),color = 'b',alpha = 0.7, linewidth = 1.0, linestyle = '--', label='down')
l3, = plt.plot(x,func_normal_line(x),color = 'r',alpha = 0.7, linewidth = 1.0, linestyle = '--', label='down')
l4, = plt.plot(2, y1, color = 'r', marker='.', markersize = 20)
# 传参到handles里必须复制后加上','
# 定义图例
# labels会替换掉线性的label
plt.legend(handles=[l1, l2,l3], labels=['curve', 'tangent','normal'], loc= 'best')
plt.axis("equal")
plt.show()