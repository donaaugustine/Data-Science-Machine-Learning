import numpy as np
arr=np.arange(1,21,1,dtype=float)
print("1D array with 20 elements:\n",arr)

odd=np.arange(1,20*2,2)
print("Odd Array : ",odd)

mat=odd.reshape(5,4)
print("Reshape array to 5x4 matrix:\n",mat)


print("Display the elements of rows 2 to 5 and columns 1 to 3:")
print(mat[1:5 , 0:3])

print("Display the elements of 2nd and 3rd column:")
print(mat[:,1:3])

l=mat[-1]
print("Last row:",l)
print("Display last 2 elements of last row:")
print(l[-2:])
