import numpy as np 
import matplotlib.pyplot as plt

fig = plt.figure(figsize =(10,10), dpi=80)#创建画布，大小10x10，像素80
x = np.linspace(0,1,1000) #numpy 产生随机数
fig.add_subplot(211) #2x1图形，选择第一个图片绘制
plt.title('y=x^2 or y=x')#添加标题
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#设置x轴范围（0，1）
plt.ylim((0,1))#设置y轴范围（0，1）
plt.xticks([0,0.3,0.6,1])#设置x轴刻度
plt.yticks([0,0.5,1])#设置y轴刻度
plt.plot(x, x**2)#y=x^2
plt.plot(x, x)#曲线2 y=x
plt.legend(['y=x^2','y=x'])#添加图列
plt.savefig('./Phase2/整体绘图流程.png')#保存图片
plt.show()