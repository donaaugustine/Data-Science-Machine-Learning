import numpy as np
print("Uninitialized Array")
a = np.full([2, 3], None)
print(a)

b = np.ones(3,dtype=int)
print("Array with all elements 1 : ",b)

c = np.zeros(3,dtype=int)
print("Array with all elements 0 : ",c)