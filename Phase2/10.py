import numpy as np 
import matplotlib.pyplot as plt

strike = np.linspace(50,150,24)
ttm = np.linspace(0.5,2.5,24)
strike,ttm = np.meshgrid(strike, ttm)

#产生一组虚假的隐含波动率
iv = (strike - 100 ) ** 2/ ( 100 * strike) / ttm

#生成波动率图标
fig = plt.figure(figsize=(9,6))
ax = fig.gca(projection='3d')
surf = ax.plot_surface(strike, ttm, iv, rstride=2, cstride=2, cmap=plt.cm.coolwarm,lw=0.5,antialiased=True)
ax.set_xlabel('strike')
ax.set_ylabel('time_to_maturity')
ax.set_zlabel('implied volatility')
#set view不同参数代表不同视角
ax.view_init(30, 60)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("./Phase2/example_3D.png")
plt.show()