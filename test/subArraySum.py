def balancedSums(arr):
    if n == 1:
        return 'YES'
    sumL = 0
    sumR = 0
    i =0
    j = n-1
    while i <= j:
        if i ==j and sumL == sumR:
            return 'YES'
        elif sumL > sumR:
            sumR+=arr[j]
            j =j-1
        else:
            sumL+=arr[i]
            i =i +1

    return 'NO'

arr = [0 ,0 ,2, 0]
n = len(arr)
print(balancedSums(arr))