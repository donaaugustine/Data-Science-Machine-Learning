import numpy as np

arr=np.array([[1,2,3,4],[5,6,7,8],[1,4,2,7],[3,1,8,9]])
print("The original array is : \n", arr)

print("Array with all elements excluding first row :\n",arr[1:])

print("Array with 3rd and 4th element of 1st row : \n",arr[0,2:4])