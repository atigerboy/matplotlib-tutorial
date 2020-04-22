import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(10, 6), dpi=80)
x = range(10)
y = np.sort(np.random.uniform(1,10,10))
# 在figure中，距离左侧和底部各figure的10%的宽度，创建子窗口，长宽各为figure的80%
left,bottom,width,height = 0.1,0.1,0.8,0.8
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r',alpha=.5)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height = 0.2,0.6,.25,.25
ax2 = fig.add_axes([left,bottom,width,height])
ax2.plot(x,y,'g',alpha=.5)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

plt.axes([.6,.2,.25,.25])
# 这里的plt设置的是上面这行的axes状态
plt.plot(y[::-1],x,'y')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()