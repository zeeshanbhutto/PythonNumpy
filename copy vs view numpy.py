import numpy as np
var=np.array([1,2,3,4])
co=var.copy()
print("var",var)
print("copy",co)
#The copy owns the data./The view dosent owns the data.
#The copy of the array is new array./it provide just view of orignal copy.
#The copy data dosent effict by changing orignal one/while view will show changes when it will done in orignal one.
x=np.array([9,8,7,6,5,4])
vi=x.view()
x[1]=40
print("x",x)
print("vi",vi)

