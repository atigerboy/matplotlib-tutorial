import numpy as np
import sys
import traceback
a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b # a.size == b.size
d = b**2 # element ** 2
e = 10*np.sin(a)
f = a<35

### Matrix 
A = np.array([[1,1],[0,1]])
B = np.array([[2,0],[3,4]])
C = A * B #element wise product ([2,0],[0,4])
D = A @ B #matrix product
E = A.dot(B)#same result as A@B

#### *= +=,notes dtype implict convert!
rg = np.random.default_rng(1)
A1 = np.ones((2,3),dtype=int)
B1 = rg.random((2,3))#random 
A1 += 3
B1 += A1
try:
    A1+=B1
except Exception as err:
    print(traceback.format_exc())

### common built-in function
print(B1)
print( B1.sum(), B1.min(), B1.max())
print( B1.sum(axis=0),B1.min(axis=1),B1.max(axis=0))#sum of each colum
#序列和，cs[1]=x[1] cs[2]=x[1]+x[2],cs[3]=cs[2]+x[3],用在累计概率上吧
print(B1.cumsum(axis=1))#cumulative sum along each row, 
print(np.exp(B1))
print(np.sqrt(B1))

