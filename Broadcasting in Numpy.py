#broadcasting is the powerfull feature in the Numpy as the popular numerical computing library that allows you to perform element_wise
# operation between arrays of different shape
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([10, 20, 30])

result = A + B
print(result)
# now we are going to see one more examample...
a=np.array([1,2,3])
print(a)
print(a.shape)
print()
b=np.array([[1],[2],[3]])
print(b)
print(b.shape)
print()
print(a+b)