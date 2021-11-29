#Write a program to find the sum of 2 matrices using nested List.

a = []
a1 = [1, 2, 3]
a.append(a1)
a2 = [4, 5, 6]
a.append(a2)
print(a)



b =[]
b1 = [1, 1, 3]
b.append(b1)
b2 = [2, 4, 2]
b.append(b2)
print(b)

result = [[0,0,0],
          [0,0,0]]

print("Resultant matrix : ")
for i in range(len(a)):
   for j in range(len(a[0])):
       result[i][j] = a[i][j] + b[i][j]
for r in result:
   print(r)