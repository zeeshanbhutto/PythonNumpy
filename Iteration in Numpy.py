#now we are going to discus about iteration in numpy array where we itterate our array as follow,
import numpy as np
var=np.array([1,2,3,4,5,6,7,8,9])
for i in var:
    print(i)

#now we are going to iterate 2D array
var1=np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(var1)
print(var1.ndim)
for j in var1:#this is known as row iteration.
    print(j)
print()

for k in var1:
    for l in k:
        print(l)
#okk now we are going to see that how to itterate three dimension arrays...
var3=np.array([[[1,2,3],[4,5,6]]])
print(var3)
print(var3.ndim)
print()
for q in var3:
     for x in q:
         for z in x:
             print(z)

var3=np.array([[[1,2,3,5],[4,5,6,6]]])
print(var3)
print(var3.ndim)
for i in np.nditer(var3):#nditer fun is used to iterate all numbers in a triple dimension.
    print(i)
#if you want to iterate the idex numbers with values then you will use ndenumerate.
var3=np.array([[[1,2,3,5],[4,5,6,6]]])
print(var3)
print(var3.ndim)
for i,d in np.ndenumerate(var3):
    print(i,d)