#in this second file we are going to see that how to create numpy arry with different functions....
import numpy as np
arr=np.array([1,2,3])
print(type(arr))# basic revision
#here we are going to especial numpy arrays like we are going to create an array filled with 0's.
arr_zero=np.zeros(5)
print(arr_zero)
#okk but i want two dimensional array by using the same function so let see....
arr_zero1=np.zeros((3,4))
print(arr_zero1)# here you can see two dimensional array by the same fun..

#another especial numpy array ,to create an array filled with 1's.
arr_one=np.ones(3)
print(arr_one)
#now we are going to see how to create an empty array
arr_em=np.empty(4)
print(arr_em)#the previously data stored in your memory is known as empty array.

#now we are going to create an especial numpy array by using
arr_range=np.arange(5)
print(arr_range)
#an array digonal filled with 1's.
arr_dig=np.eye(3)
print(arr_dig)
#now we are going to create an array with values that are spaced linearly in a specified interval.
arr_lin=np.linspace(0,20,num=5)
print(arr_lin)



