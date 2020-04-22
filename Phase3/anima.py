import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

fig,ax = plt.subplots()
fig.set_figwidth(7)
fig.set_figheight(7)
x = np.arange(0,8*np.pi,0.01)
line, = ax.plot(x,np.sin(x),'c-.',linewidth=3,alpha=.8)

def animate(i):
    line.set_ydata(np.sin(x+i/50))
    return line,

def init():
    line.set_ydata(np.sin(x))
    return line,
    
'''
定义动画,FuncAnimation为其中一种方法
传入一个fig,func就是传入一个animating的func，frames表示总帧数，init_func为动画的第一帧，
interval为更新频率，blit是不是要更新变化点，没有变化点不更新.整图更新为False
'''
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,
                              init_func=init,interval=20,
                              blit=False
                             )
plt.show()