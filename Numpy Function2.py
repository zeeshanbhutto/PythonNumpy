import numpy as np
zee=np.array([1,2,3,4,5,6])
np.random.shuffle(zee)
print(zee)

zee1=np.array([1,2,3,3,4,2,3,4,3,5,3,4,5,6])
x=np.unique(zee1,return_index=True)
print(x)

zee2=np.array([1,2,3,4,5,6])
x=np.resize(zee2,(2,3))
print(x)
#flatten is a keyword which will convert your array 2D into 1 D array.
zee2=np.array([1,2,3,4,5,6])
x=np.resize(zee2,(2,3))
print(x)
print(x.flatten(order="f"))


