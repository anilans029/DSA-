import time

def partition_algorithm(arr,i,j):
    pivot = i
    k = i
    l = i+1
    while(l <= j):
        if arr[l]> arr[pivot]:
            l += 1
        elif arr[l]<=arr[pivot]:
            k += 1
            arr[k],arr[l] = arr[l],arr[k]
            l += 1
    arr[pivot],arr[k] = arr[k],arr[pivot]
    return k

def quickSort(arr,i,j):
    if i == j:
        return arr
    elif i<j:
        pivot = partition_algorithm(arr,i,j)
        quickSort(arr,i,pivot-1)
        quickSort(arr,pivot+1,j)
        return arr

start = time.time()
arr = [10,20,30,15,25.5,6,2,10,20]
first = 0
last = len(arr) -1
arr = quickSort(arr,first,last)
print(arr)
end = time.time()
print(f"the time taken for execution is {end - start}")