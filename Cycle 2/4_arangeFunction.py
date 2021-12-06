import numpy as np

a = np.arange(1, 11, 1)
print(a)
element1 = a[:4]
print("First 4 elements : ",element1)
element2 = a[4:]
print("Last 6 elements : ",element2)
element3 = a[2:8]
print("index 2 to 7 : ",element3)