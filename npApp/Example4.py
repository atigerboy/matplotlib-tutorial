import numpy as np
## indexing ,slicing and iterating
a = list(range(10)) 
a = [i ** 3 for i in a ]
print(a)
print(a[2:5])
print(a)
print(a[::-1])
# a[:6:2] = 1000 #for normal list, ! support

a = np.arange(10)**3#element wise  pow
print(a)
print(a[2:5])#like list
a[:6:2]=1000
print(a)
b = a[::-1]
for i in a:
    print(i**(1/3.),end=",")

#Multidimensional arrays can have one index per axis.
#These indices are given in a tuple separated by commas
def f(x,y):
    return 10*x+y
b = np.fromfunction(f, (5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5,1])#each row in the second column of b
print(b[: ,1])
print(b[1:3, : ]) 
print(b[-1]) #last row,