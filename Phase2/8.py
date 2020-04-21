import numpy as np 
import matplotlib.pyplot as plt

fig = plt.figure(figsize =(7,10), dpi=80)#创建画布，大小10x10，像素80
np.random.seed(2000)
month=['Jan','Fed','Mar','Apr']
y = np.linspace(10, 80,4) 
x = list(range(4))

fig.add_subplot(321) #2x2图形，垂直
#分别为两条数据增加图列
plt.xticks(x,month)
plt.bar(x, y)
plt.title('BAR Example')
plt.grid(True)

fig.add_subplot(322) #2x2图形，水平
#分别为两条数据增加图列
plt.yticks(x,month)
plt.barh(x, y)
plt.title('BARH Example')
plt.grid(True)

y = np.random.standard_normal((1000,2))
c = np.random.randint(0,10, len(y))
fig.add_subplot(323) #2x2图形，散点图
#分别为两条数据增加图列
plt.scatter(y[:,0],y[:,1],c=c,marker='o')#通过scatter函数加入三维数据
plt.colorbar()
plt.xlabel('1st')
plt.ylabel('2nd')
plt.axis('tight')
plt.title('SCATTER Example')
plt.grid(True)

fig.add_subplot(324) #2x2图形，散点图
#分别为两条数据增加图列
plt.hist(y,label=['1st','2nd'], bins=25)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.legend()
plt.title('HIST Example')
plt.grid(True)

#pie 
fig.add_subplot(325) #2x2图形，散点图
#分别为两条数据增加图列
plt.pie(list(range(10,110,10)),labels=list("abcdefghjk"),autopct="%.2f%%")
plt.axis('equal')
plt.grid(True)
plt.title("PIE Example")

#boxplot
fig.add_subplot(236) #2x2图形，
#分别为两条数据增加图列
plt.boxplot(y)
plt.grid(True)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.legend()
plt.title('BOXPLOT Example')



plt.savefig('./Phase2/example_plt.png')#保存图片
plt.show()