def bubbleSort(arr):
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []
n = int(input("Enter limit :"))
print("Enter elements :")
for i in range(0,n):
    arr.append(int(input()))

bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i])