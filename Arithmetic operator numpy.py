#now we are going to check about arithmatic operator innumpy array,like add,sub,mul,divide,modulus,power,reciprocal,etc.
#adding a single value in all array.
import numpy as np
var = np.array([1,2,3,4])
varadd= var + 3
print(varadd)
#we can also add two numpy arrays....
var1 = np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd= var1 + var2
print(varadd)

var1 = np.array([2,3,4])#multiplication of two arays.
var2 = np.array([2,3,4])
varmul= var1 * var2
print(varmul)

var1 = np.array([12,6,4])#division of two arays.
var2 = np.array([2,2,2])
vardiv= var1 / var2
print(vardiv)
#we can also perform these function with the help of numpy functions.
var1 = np.array([12,6,4])
var2 = np.array([2,2,2])
varadd=np.add(var1,var2)
print(varadd)
#now we are going to talk about 2D array and imlement all these operators in it.
print()
var_1=np.array([[2,4,6,8],[2,4,6,8]])
var_2=np.array([[2,4,6,8],[2,4,6,8]])
print(var_1)
print()
print(var_2)
print()
var_add=var_1 + var_2
print(var_add)
print()
#now we are going to see the reciprocal operator in numpy array
var = np.array([1,2,3,4])
varadd=np.reciprocal(var)
print(varadd)








