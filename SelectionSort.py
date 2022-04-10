# the time complexity for the selection sort is O(n^2)

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[i]
        for j in range(i+1,n):
            if arr[j] < min :
                arr[i],arr[j] = arr[j],arr[i]
                min = arr[i]
    return arr

arr = [10,14,67,32,59,89,674,200,20,400,53,15,36,74,36]
arr = selectionSort(arr)
print(arr)