import numpy as np
n = int(input("How many elements you want? : "))
n = 2*n
a=np.arange(0,n,2)
print("Even Array : ",a)

print("Elements from index 2 to 8 : ",a[2:9])
x = slice(2,9)
print("Elements from 2 to 8 using slice() : ",a[x])

print("Last 3 Elements:",a[-3:])

b = a[::2]
print("Alternate elements : ",b)

print("Last 3 Alternate Numbers:",b[-3:])