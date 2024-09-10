#now we are going to see data types in numpy array.let see
#1)boolean(true or false)sorted by byte.
#2)int default integer type
#3)intcidentical to c int
#4)intpinteger used for indexing
#5)int8 Byte(-128,127)
#6)float shorthand for float64
#7)complex shorthand for complex 128
import numpy as np
var =np.array([1,2,3,4,5,6,7,8,9,10])
print("Data type:",var.dtype)

var =np.array([1.5,1.3,1.4,1.7])
print("Data type:",var.dtype)

var =np.array(["a","s","d"])#string data type.
print("Data type:",var.dtype)

var =np.array([1,2,3,"s","a","f"])

print("Data type:",var.dtype)
#now the intresting fact is that we canchange the datatypes of our array.
x=np.array([1,2,3,4],dtype=np.int8)
print("Datatype:",x.dtype)

x=np.array([1,2,3,4],dtype="f")#this is another short methoad to change the data type.
print("Datatype:",x.dtype)

#we can also use the data type as afunction for example.
x1=np.array([1,2,3,4])
new=np.float32(x1)
print("Datatype:",x1.dtype)
print(new)
print(x1)
print("Datatype",new.dtype)

x2=np.array([1,2,3,4])
new_one=x2.astype(float)
print(x2)
print(new_one)