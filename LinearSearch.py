
# the time complexity for searching using this linear search is O(n)
def linearSearch(arr,key):
    for i in range(0, len(arr)):
        if arr[i]== key:
            return i

arr = [43,63,75,86,234,74,23,11,644,83,3,2,66]
key = 66
key_loc = linearSearch(arr,key)
print(f"the key is found at :{key_loc}")