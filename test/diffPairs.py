def binarySearch(arr,val,start,end):
    if start <= end:
        m = start + (end-start)//2
        elem = arr[m]
        if val == elem:
            return elem
        elif val < elem:
            return binarySearch(arr,val,m+1,end)
        else:
            return binarySearch(arr,val,start,m-1)

    return None
# Complete the pairs function below.
def pairs(k, arr):
    res = []
    arr.sort(reverse = True)
    for i in range(n):
       val = binarySearch(arr,arr[i]-k,i+1,n-1)
       if val:
           res.append(tuple([arr[i],val]))
    return res

k = 2
arr = [1,3,5,8,6,4,2]
n = len(arr)
print(pairs(k,arr))