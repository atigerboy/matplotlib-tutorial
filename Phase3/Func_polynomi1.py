import matplotlib.pyplot as plt
import numpy as np
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False 


# 定义点
x = np.linspace(-3, 3, 50)
# 定义线
y1 = 2*x + 1
y2 = x**2

# plt.figure()
# plt.plot(x,y1)
# 定义窗体
plt.figure(num=3, figsize=(8,5))
# 定义轴长
plt.xlim((-1,2))
plt.ylim((-2,3))
# 定义轴名
plt.xlabel('xlabel')
plt.xlabel('ylabel')

new_ticks =  np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
# 定义轴点替换标签
plt.yticks([-2, -1.6, -1, 1.22, 3],
          [r'$really\ bad$', r'$bad$',r'$normal\ \alpha$',r'$good$',r'$really\ good$'])

# gca = "get current axis"
# 脊梁偏移
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -.5))
ax.spines['left'].set_position(('data',0))
# outward, axes

l1, = plt.plot(x,y2,label = 'up', color = 'b', alpha = 0.7 )
l2, = plt.plot(x,y1,color = 'red',alpha = 0.7, linewidth = 1.0, linestyle = '--', label='down')
# 传参到handles里必须复制后加上','
# 定义图例
# labels会替换掉线性的label
plt.legend(handles=[l1, l2], labels=['blue line', 'red line'], loc= 'best')
plt.show()