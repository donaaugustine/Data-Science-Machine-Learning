#Program to check whether a given number is perfect number or not(sum of factors =number)

n = int(input(" Please Enter any Number: "))
Sum = 0
for i in range(1, n):
    if(n % i == 0):
        Sum = Sum + i
if (Sum == n):
    print(" %d is a Perfect Number" %n)
else:
    print(" %d is not a Perfect Number" %n)