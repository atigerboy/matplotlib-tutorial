import numpy as np 

a = np.arange(15).reshape(3,5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name)
#the size in bytes of each element of the array, sizeof(int32)
print(a.itemsize)
print(a.size)
print(type(a))
print(a.data)

