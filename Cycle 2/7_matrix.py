import numpy as np

M1 = np.array([[9, 2], [5, 8]])
M2 = np.array([[3, 4], [1, 4]])
print("First matrix \n ",M1)
print("Second matrix \n ",M2)
add = M1 + M2  
print("Matrix addition\n",add)

sub = M1 - M2  
print("Matrix Substract\n",sub)

mul = M1 * M2
print("Multiply the individual elements of matrix\n",mul) 

div = M1 / M2  
print("Divide the elements of the matrices\n",div)

M3 = M1.dot(M2) 
print("matrix multiplication \n",M3) 

tr = M1.transpose()
print("Transpose of the First matrix\n",tr) 

print("Sum of diagonal elements of first matrix") 
print(np.trace(M1))