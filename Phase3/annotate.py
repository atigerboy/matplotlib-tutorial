import matplotlib.pyplot as plt
import numpy as np
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False 

# 定义点
x = np.linspace(-3, 3, 50)

plt.figure(num=1, figsize=(8,5))
y1 = 2*x + 1
l1, = plt.plot(x,y1, alpha=0.7, color='b')
# 脊梁偏移
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0 + 1
# 定义注释点
p1 = plt.scatter(x0, y0, s= 50 , c='r')
# 定义注释点至坐标的线
plt.plot([x0,x0],[y0, 0],'k--',lw=2.0)

# method 1
############################### 
# 定义注释
plt.annotate(
             # 注释文本   
             r'$2x + 1 = %s$'% y0, 
             # 注释以当前data为中心
             xy=(x0,y0), xycoords='data',
             # 注释偏移
             xytext=(+30,-30), textcoords='offset points', fontsize=15 , 
             # 注释图形,注释弧度等
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2')
             )
# method 2
############################### 
plt.text(-4.0,3, r'$This\ is\ the\ some\ tag.\ \t\mu\ \sigma_i\ \alpha_t$',
        fontdict={'size':16, 'color':'y'})

# 定义图例
plt.legend(handles=[p1, l1,], labels=['point', 'line',], loc= 'best')

plt.show()