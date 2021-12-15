import numpy as np
mat = np.array([[6, 1, 1, 4],
              [1, 2, 5, 2],
              [1, 5, 7, 3],
              [3, 2, 4, 1]])
print("Original Matrix....\n",mat)  
sub = mat[1:3, 1:3] 
print("Sub matrix....\n",sub)
mat2 = np.array([[1, 4],
              [3, 2]])
print("Second matrix is....\n",mat2)
mul=np.dot(sub,mat2)
print("Multiplication...\n",mul)
mat[1:3, 1:3] = mul
print("Initial matrix after replacement..\n",mat)