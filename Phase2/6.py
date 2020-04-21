import numpy as np 
import matplotlib.pyplot as plt

fig = plt.figure(figsize =(7,10), dpi=80)#创建画布，大小10x10，像素80
np.random.seed(2000)
x = np.random.standard_normal((20,2)).cumsum(axis=0) #numpy 产生二维正太分布函数
fig.add_subplot(111) #1x1图形，选择第一个图片绘制
#分别为两条数据增加图列
plt.plot(x[:,0], lw=1.5,label='1st')# line mode,set line width
plt.plot(x[:,1], lw=1.5,label='2nd')# line mode,set line width
plt.plot(x, 'rd') # point mode,only set color
plt.grid(True)
plt.axis('tight')
plt.legend(loc='upper left')#实用数字是无效的，实用方位比较合适，用bbox_to_anchor定义具体位置
plt.xlabel('index')
plt.ylabel('value')
plt.title('Axis Example')
plt.savefig('./Phase2/example_axis.png')#保存图片
plt.show()