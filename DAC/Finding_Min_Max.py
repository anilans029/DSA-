import time

# the time complexity of Finding MinMax using divide and conquer is O(n) for all cases
# T(n) = 2T(n/2) + c  -----> O(n)

def dacMinMax(arr,i,j):

    #small condition
    if i == j :
        mx = arr[i]
        mi = arr[j]
        return mx, mi
    elif i== j-1:
        if arr[i]>arr[j]:
            mx = arr[i]
            mi = arr[j]
            return mx, mi
        else :
            mx = arr[j]
            mi  = arr[i]
            return mx,mi
    else:
        #big problem
        #dividing big problem into small problem
        m = i + (j-i)//2

        #conquer
        #perform recursion for division
        max1, min1 = dacMinMax(arr,i,m)
        max2, min2 = dacMinMax(arr,m+1,j)

        # combine
        mx = max(max1,max2)
        mi = min(min1,min2)
        return mx,mi

start = time.time()
arr = [12,5,2,63,4,13,5,6,3,6,7,3,4,2,8,56,45,3,5,34,34444]
i = 0
j = len(arr)-1
mx, mi = dacMinMax(arr,i,j)
print(mx,mi)
end = time.time()
print("the execution time of the program is: ", end - start)