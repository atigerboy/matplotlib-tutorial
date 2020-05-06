import numpy as np
a = np.array([2,3,4])
b = np.array([(1.5,2,3),(4,5,6)])
c = np.array([[1,2],[3,4]],dtype=complex)
d = np.zeros((3,4))
e = np.ones((2,3,4),dtype=np.int16)#dtype can also be specified
f = np.empty((2,3))#uninitialized
g = np.arange(10,30,5)# like range,1 row data
h = np.linspace(0,2,9) #9 numbers from 0,2(included), better than range 
i = np.linspace(0,2*np.pi, 100)
f = np.sin(i)