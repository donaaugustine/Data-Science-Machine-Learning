import numpy as np

x = np.array([[2, 4, 6,1], [6, 8, 10,1],[1, 2, 1,1], [1, 1, 1,1]])
print("4x4 2D Array :")
print(x)

print("Display all elements excluding the first row")
print(x[1:])

print("Display all elements excluding the last column")
print(x[:, :3])

print("Display the elements of 1st & 2nd column in 2nd & 3rd row")
print(x[1:3, 0:2])

print("Display the elements of 2 nd and 3 rd column")
print(x[:, 1:3])

print("Display 2 nd and 3 rd element of 1 st row")
print(x[0,1])
print(x[0,2])

print("Display the elements from indices 4 to 10 in descending order(use –values)")
a = np.array([1,2,8,9,3,4,5,6,7])
print("Array : ",a)
array_copy = np.sort(a)[::-1]
print("Sorted Array :",array_copy)
print("Index 4 to 10 : " ,array_copy[4:10])