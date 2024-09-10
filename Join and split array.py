#putting contents of two or more arrays in a single array is know as joining of arrays.
import numpy as np
var=np.array([1,2,3,4])
var1=np.array([5,6,7,8])
ar=np.concatenate((var,var1))
print(ar)
#now we are going to join 2D array
var2=np.array([[1,2],[3,4]])
var3=np.array([[5,6],[7,8]])
tar=np.concatenate((var2,var3),axis=1)
print(var2)
print()
print(var3)
print()
print(tar)
#now we are going to that how can we merge to arrays with the help of
var_1=np.array([1,2,3,4])
var_2=np.array([5,6,7,8])
ar_new=np.stack((var_1,var_2),axis=1)
print(ar_new)
ar_ne=np.hstack((var_1,var_2))#it works along row
print(ar_ne)
ar_new1=np.dstack((var_1,var_2))#it works along height
print(ar_new1)
ar_n=np.vstack((var_1,var_2))#it works along coloumn
print(ar_n)

# now we are going to see that how can we split our array in multiple array
var4=np.array([1,2,3,4,5,6,7,8,9])
print(var4)
xy=np.array_split(var4,3)
print(xy)
print(type(xy))
print()
#now we are going to see spliting in two dimension.
var4=np.array([[1,2],[3,4],[5,6]])
print(var4)
xy=np.array_split(var4,3)
print(xy)
print(type(xy))
