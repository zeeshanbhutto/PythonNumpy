#now we are going to see about insert function in numpy array.
import numpy as np
var=np.array([1,2,3,4])
print(var)
y=np.insert(var,4,5)#insert fun dosent except float value it will only except int.
print(y)
#now we are going to see that how can we work with 2D array and how to insert values in it.
var1=np.array([[1,2,3],[4,5,6]])
v1=np.insert(var1,2,6,axis=0)#you will see another row of 6 6 6 will created
print(v1)
v1=np.insert(var1,2,6,axis=1)#it will works along column
print(v1)
print()
var=np.array([1,2,3,4])
t=np.append(var,[5,6,7,8,9])
print(t)
#now we are going to see that how to do delte any thing from numpy array.
var2=np.array([1,2,3,4,5,6])
r=np.delete(var2,[2,3,4])
print(r)

