
def bubbleSort(arr):

    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr


arr = [10,14,67,32,59,89,674,200,20,400,53,15,36,74,36]
arr = bubbleSort(arr)
print(arr)