# the time complexity of the merge algorithm is O(n) in every case if both sorted arrays are of equal sizes
# if the sorted arrays are not equal size i.e, m and n then time complexity will be O(m+n) every case
# in merge alogrithe time complexity = no.of moves + no.of comparisons
def MergeAlgorithm(arr1,arr2):
    sorted_array = []
    i =0
    j =0
    len1 = len(arr1) -1
    len2 = len(arr2) -1

    while(i<=len1 and j <= len2):
        if arr1[i] < arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append((arr2[j]))
            j += 1

    len1 = len(arr1[i:])
    len2 = len(arr2[j:])
    if len1 != 0:
        sorted_array.extend(arr1[i:])
    elif len2 != 0:
        sorted_array.extend(arr2[j:])
    return sorted_array


# the total time complexity of the merge sort is O(nlogn) in every case
# T(n) = 2T(n/2) + n

def mergeSort(arr,i,j):
    if i == j :
        return arr[i:j+1]
    else:
        # divide
        m = i + (j-i)//2

        #conquer
        sorted_array1 = mergeSort(arr,i,m)
        sorted_array2 = mergeSort(arr,m+1,j)

        #combine is the main part in mergesort where it uses merge algorithm to combine
        sorted_array = MergeAlgorithm(sorted_array1,sorted_array2)
        return sorted_array

arr = [10,14,67,32,59,89,674,200,20,400,53,15,36,74,36]
i = 0
j = len(arr) -1
arr = mergeSort(arr,i,j)
print(arr)