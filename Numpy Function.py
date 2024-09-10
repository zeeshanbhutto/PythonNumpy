#There are alot of functions in numpy array like search,filter,sort,search sorted
#Search Array) search an array for a certain value,and return the indexes that get a match.we can use where keyword for searching.
import numpy as np
var= np.array([1,2,3,4,5,6,7,2,4,5,5,3])
x=np.where(var/9 ==0 )
print(x)
#search sorted array)which performs a binary search in the array and return the index where the
#especified value would be inserted to maintain the search order.
var1= np.array([1,2,3,4,6,7])
x1=np.searchsorted(var1,5 )
print(x1)
#Sort array)you can sort your sequence here asending and decending and also numeric and alphabatic.
var_2= np.array([1,4,6,7,2,4,5,3])
x=np.sort(var_2)
print(x)
print()
var_3= np.array(["s","a","z","x","b","d"])
x=np.sort(var_3)
print(x)
#now we are going to implement sort function in 2D array.
var_3= np.array([[1,4,2],[4,7,2],[7,2,4]])
print(np.sort(var_3))
#filter Array) Getting some elements out of an existing array and creating a new array out of them.
var_3= np.array(["s","a","z","x","b","d"])
f=[True,False,True,True,False,False]
print(var_3[f])