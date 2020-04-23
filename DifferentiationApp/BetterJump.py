import numpy as np 
import matplotlib.pyplot as plt

fig = plt.figure(figsize =(7,10), dpi=80)#创建画布，大小10x10，像素80

g = -9.8
vx = 4
vy0 = -g * 0.5 
t = np.linspace(0,1,40)
x = t * vx
y = 0.5 * g * t ** 2 + vy0 * t

def velCacl(t):
    return vy0 + g * t

fig.add_subplot(221) #2x2图形，垂直
#分别为两条数据增加图列
plt.xlabel("x axis ")
plt.ylabel("y axis")
plt.plot( x, y, "r",label="normal")
plt.title('Explicit Function')
plt.legend()
plt.grid(True)

fig.add_subplot(222) #2x2图形，垂直
deltaT = 1/40
y2 = []
starty,vel,_t = 0, vy0,0
for i in range(40):
    y2.append( starty)
    starty += vel * deltaT
    _t += deltaT
    vel = vy0 + g * _t  

#分别为两条数据增加图列
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot( x, y, "b")
plt.plot( x, y2,'r.',label="Euler Method")
plt.title('Euler\'s Method')
plt.legend()
plt.grid(True)

fig.add_subplot(223) #2x2图形，垂直
deltaT = 1/40
y2 = []
starty,_t = 0, 0

for i in range(40):
    y2.append( starty)
    starty = starty + ( deltaT * velCacl(_t ) 
    + 2 * deltaT * velCacl(_t + 0.5 * deltaT)
    + 2 * deltaT * velCacl(_t + 0.5 * deltaT)
    + deltaT * velCacl(_t + deltaT )
    ) /6
    _t += deltaT


#分别为两条数据增加图列
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot( x, y, "b")
plt.plot( x, y2,'r.',label="RK4 Method")
plt.title('RK4\'s Method')
plt.legend()
plt.grid(True)


fig.add_subplot(224) #2x2图形，垂直
deltaT = 1/40
y2 = []
starty,vel= 0, vy0

for i in range(40):
    y2.append( starty)
    starty += vel * deltaT + 0.5*g*deltaT *deltaT
    vel += g * deltaT 

#分别为两条数据增加图列
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot( x, y, "b")
plt.plot( x, y2,'r.',label="Verlet Method")
plt.title('Better Jump\'s Method')
plt.legend()
plt.grid(True)

plt.savefig('./DifferentiationApp/example_better_jump.png')#保存图片
plt.show()