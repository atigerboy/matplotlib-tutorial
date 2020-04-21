import numpy as np 
import matplotlib 
from matplotlib import pyplot as plt


fig = plt.figure(figsize =(10,10), dpi=80)#创建画布，大小10x10，像素80
x = np.linspace(0,1,1000) #numpy 产生随机数
fig.add_subplot(221) #2x2图形，选择第一个图片绘制
matplotlib.style.use('default')
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
fig.add_subplot(2,2,2)#2x2,第二张图
matplotlib.style.use('default')
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

fig.add_subplot(2,2,3)#2x2,第3张图
matplotlib.style.use('default')
matplotlib.rc('font', family='sans-serif', style="normal",variant="normal", size=32)
plt.plot(x, np.sin(x))
plt.title('y=sin(x)')
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#设置x轴范围（0，1）
plt.ylim((0,1))#设置y轴范围（0，1）
plt.xticks([0,0.3,0.6,1])#设置x轴刻度
plt.yticks([0,0.5,1])#设置y轴刻度
plt.legend(['y=sin(x)'])#添加图列

fig.add_subplot(2,2,4)#2x2,第4张图
matplotlib.style.use('default')
plt.rcParams['axes.edgecolor'] = 'b'  # 轴颜色设置为蓝色
plt.rcParams['axes.grid'] = True  # 添加网格
plt.rcParams['axes.spines.top'] = False  # 去除顶部轴
plt.rcParams['axes.spines.right'] = False  # 去除右侧轴
plt.rcParams['axes.xmargin'] = 0.1  # x轴余留为区间长度的0.1倍

plt.plot(x, np.sin(x))
plt.title('y=sin(x)')
plt.xlabel('x')#添加x轴名称
plt.ylabel('y')#添加y轴名称
plt.xlim((0,1))#设置x轴范围（0，1）
plt.ylim((0,1))#设置y轴范围（0，1）
plt.xticks([0,0.3,0.6,1])#设置x轴刻度
plt.yticks([0,0.5,1])#设置y轴刻度
plt.legend(['y=sin(x)'])#添加图列

plt.savefig('./Phase2/rc_Other.png')#保存图片
plt.show()