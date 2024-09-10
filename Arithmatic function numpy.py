#now we are going to see about numpy arithmatic function which can be used...
import numpy as np
var=np.array([1,2,4,3,7,9,8,6])#if you want to find the position so here you can also do that by using argmin or argmav
print(np.min(var),np.argmin(var))
print(np.max(var),np.argmax(var))
#we can also find the square root and square of this array by using numpy fun
print(np.sqrt(var))
print()
print(np.square(var))
print()
#now we are going to talk about 2D array to implrmrnt these fun.......
var_1=np.array([[5,1,3],[4,2,6]])
print(np.min(var_1,axis=1))#there are mainly two axis one is row=1 and the coloumn=0
print(np.max(var_1,axis=1))
#we can also find the values of sin and cos for array.
var2=np.array([1,2,3,4])
print(np.sin(var2))
var3=np.array([1,2,3])
print(np.cos(var3))
#here we have one last function cumulative sum "cumsum()"
var=np.array([1,2,3,4,5])
print(np.cumsum(var))