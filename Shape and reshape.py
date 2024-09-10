#now we are going to see the shape and reshape fun() in numpy
import numpy as np
var=np.array([[1,2,3,4],[1,2,3,4]])
print(var)
print()
print(np.shape(var))

var1=np.array([1,2,3],ndmin=7)
print(var1)
print(var1.ndim)
print(np.shape(var1))
#now we are going to see that how to reshape the numpy arrays.
var2=np.array([1,2,3,4,5,6])
x=var2.reshape(2,3)
print(x)
#now we are going to reshape an array of numpy which is three dimension.
var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=var3.reshape(2,3,2)
print(var3)
print()
print(y)
print(np.ndim(y))
print()
one=y.reshape(-1)
print(one)
