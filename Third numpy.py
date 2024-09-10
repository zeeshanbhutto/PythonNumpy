#now we are going to see that how can we create numpy aarray through random Numbers...
# 1)rand() the function is used to generate a random value between 0 to 1. so lets create.........
import numpy as np
var = np.random.rand(3)
print(var)
#2)randn() the function is used to generate a random value close to zero.
var_1 = np.random.randn(4)
print(var_1)
#3)ranf() the function is used to generate a random value in flot like 0.0 t0 1.0.
var_2=np.random.ranf(3)
print(var_2)
#3)randint() fun is used to generate a random numbe between two values.
var_3=np.random.randint(0,10,4)
print(var_3)

