

def DAC_BinarySearch(arr,i,j,key):
    if i == j:
        if arr[i] == key:
            return i
        else:
            return -1
    else:
        # divide
        mid = i + (j-i)//2

        # conquer but no combine because binary search is parital DAC application
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            pos = DAC_BinarySearch(arr,i, mid-1,key)
            return pos
        else:
            pos = DAC_BinarySearch(arr,mid+1,j,key)
            return pos
arr = [10,15,16,25,45,54,65,87,98,4005]
key = 98
i = 0
j = len(arr) -1
pos = DAC_BinarySearch(arr,i,j,key)
if pos != -1:
    print(f"the position of the key {key} is {pos}")
else:
    print("the key is not found")