#marix and numpy are almost same but the difference you will face in both cases will be in their multiplication.
import numpy as np
var=np.matrix([[1,2,3],[4,5,6]])
print(var)
print(type(var))
var=np.array([[1,2,3],[4,5,6]])
print(var)
#both matrix and numpy array are looking same in output.so what the different to use??
print(type(var))
#ok we will check their difference between by using mathematics operator
var=np.matrix([[1,2],[4,5]])
var2=np.matrix([[1,2],[4,5]])
print(var+var2)#it will add your metoad successfully but at the other place
#print(var*var2)#if you go for mul it will give you an error that your shape are not same
print(var.dot(var2))#here you can revice your broadcast topic
#now we are going to see numpy matrix function which we can use for our mathematic calculations.
#like transpose in which matrix will change it axis.
print()

var3=np.matrix([[1,2,3],[4,5,6]])
print(var3)
print(np.transpose(var3))
print(np.swapaxes(var3,0,1))#it works same as transpose do
var4=np.matrix([[1,2],[3,4]])
print()
print(np.linalg.inv(var4))#this fun will give you inverse of matrix.
var5=np.matrix([[1,2],[3,4]])
print(var5)
print(np.linalg.matrix_power(var5,2))
print(np.linalg.matrix_power(var5,0))#this is know as identity matrix
print()
var=np.matrix([[1,2],[4,5]])#this is how to find a determinant
print(np.linalg.det(var))

