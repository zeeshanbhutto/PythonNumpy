#here first of all we are going to talk about indexing in numpay. we can check indexing of single,double and triple dimension arrrays.
import numpy as np
a=np.array([1,2,3,4,5])
print(a[1])
print(a[-3])
print()
#now we are going to find indexing in two dimension array.
var1=np.array([[1,2,3,4],[1,2,3,4]])
print(var1)
print(var1.ndim)
print()
print(var1[1,3])
print()
#now we are going to create three dimension array in which we see how to do indexing
var2=np.array([[[1,2],[3,4]]])
print(var2)
print(var2.ndim)
print()
print(var2[0,1,1])
#now we going to see how to do slicing in numpy
var3=np.array([1,2,3,4,5,6,7,8])
print(var3)
print()
print("2 to 6",var3[2:7])
print("1 to end",var3[0:])
#now we are going to study about slicing in 2D array..
var4=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,7,5]])
print(var4)
print(var4.ndim)
print()
print(var4[2,2:5])
