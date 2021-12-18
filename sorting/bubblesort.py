print("this is bubble sorting")
def bubbleSort(arr):
    print(arr)
    n= len(arr)
    for i in range (n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[12,23,123,9,13,1]
bubbleSort(arr)

print("result")
for i in range (len(arr)):
    print(arr[i])