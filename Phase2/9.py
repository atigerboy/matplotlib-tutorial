import numpy as np 
import matplotlib.pyplot as plt

#第一步：定义求取积分的函数
def func(x):
    return 0.5* np.exp(x) + 1

#第二步：定义积分区间，生成必须是整数值？
a,b= 0.5,1.5
x = np.linspace(0,2)
y = func(x)

#第三步：绘制函数图像
fig,ax = plt.subplots(figsize=(7,5))
plt.plot(x, y, 'b',lw=2)
plt.ylim(ymin=0)

#第四步：实用polygon函数生成阴影部分，表示积分面积
Ix = np.linspace(a,b)
Iy = func(Ix)

verts = [(a,0)] + list(zip(Ix,Iy)) + [(b,0)]
poly = plt.Polygon(verts,facecolor='0.7',edgecolor='0.5')
ax.add_patch(poly)

#第五步：实用plt.tex和plt.figtext在图表上添加数学公式和一些坐标轴标签
plt.text(0.5*(a+b),1,r"$\int_a^b f(x)\mathrm{d}x$",horizontalalignment='center',fontsize=20)
plt.figtext(0.9, 0.075,'$x$')
plt.figtext(0.075,0.9,"$f(x)$")

#第六步：设置刻度标签以及添加网格
ax.set_xticks((a,b))
ax.set_xticklabels(('$a$','$b$'))
ax.set_yticks([func(a),func(b)])
ax.set_yticklabels(('$f(x)$','$f(b)$'))
plt.grid(True)
plt.savefig("./Phase2/function_curve.png")
plt.show()