#hellow welcome this is our first file for learning basics of numpy....
import numpy as np
x=np.array([1,2,3,4])
print(x)
print(type(x))
print(x.ndim)#by using this function you can find the nature of array either it is one two or three D array.

y=[1,2,3,4]
print(y)
print(type(y))
l=[]
for i in range(1,5):
    int_1=int(input("Enter your numbr:-"))
    l.append(int_1)
    print(np.array(l))

#in numpy we can create 1D ARARAY, 2D ARRAY, 3DARRAY, HIGHER DIMENSIONAL ARRAY.ok now we are going to create 2D array.
arr2=np.array([[1,2,3,4],[1,2,3,4]])
print(arr2)
print(arr2.ndim)

#now we are going to see three dimensional array.
arr3=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(arr3)
print(arr3.ndim)

#now we are going to create multidimentional array in below code.
arrn=np.array([1,2,3],ndmin=8)
print(arrn)
print(arrn.ndim)

















