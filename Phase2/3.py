import numpy as np 
import matplotlib 
from matplotlib import pyplot as plt

print(matplotlib.rc_params)
print(matplotlib.rcParamsDefault)
print(matplotlib.rcParams)

fig = plt.figure(figsize =(10,10), dpi=80)#创建画布，大小10x10，像素80
x = np.linspace(0,1,1000) #numpy 产生随机数
fig.add_subplot(211) #2x1图形，选择第一个图片绘制
plt.rcParams['lines.linestyle'] = 'dashdot'#修改线类型
plt.rcParams['lines.linewidth'] = 1 #修改线宽

plt.title('y=x')#添加标题
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#设置x轴范围（0，1）
plt.ylim((0,1))#设置y轴范围（0，1）
plt.xticks([0,0.3,0.6,1])#设置x轴刻度
plt.yticks([0,0.5,1])#设置y轴刻度
plt.plot(x, x)#曲线2 y=x
plt.legend(['y=x'])#添加图列
#添加第二张图
fig.add_subplot(2,1,2)#2x1,第二张图
matplotlib.rc('lines', linestyle='--', linewidth=1.5)
plt.plot(x, x**2)
plt.title('y=x^2')
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#设置x轴范围（0，1）
plt.ylim((0,1))#设置y轴范围（0，1）
plt.xticks([0,0.3,0.6,1])#设置x轴刻度
plt.yticks([0,0.5,1])#设置y轴刻度
plt.legend(['y=x^2'])#添加图列

plt.savefig('./Phase2/rcParams.png')#保存图片
plt.show()