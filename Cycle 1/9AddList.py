#Write a program to add elements of  given 2 lists

l1 = []
print("Enter number of elements in list1 : ")
n1 = int(input())
print("Enter elements in list1 : ")
for i in range(0, n1):
    ele1 = int(input())
    l1.append(ele1)
print("List 1 : ", l1)

l2 = []
print("Enter number of elements in list2 : ")
n2 = int(input())
print("Enter elements in list2 : ")
for i in range(0, n2):
    ele2 = int(input())
    l2.append(ele2)
print("List 2 : ", l2)

result = []
for i in range(0, len(l1)):
    result.append(l1[i] + l2[i])

print("Resultant list is : " + str(result))