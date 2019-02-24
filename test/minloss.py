import sys
def minimumLoss(price):
    piMap = []
    for i in range(0,len(price)):
        piMap.append(tuple([price[i],i]))
    piMap.sort(key=lambda x: x[0], reverse=True)
    min = sys.maxsize
    minIndex = -1
    for i in range(0,n-1):
        temp =  (piMap[i][0]) - (piMap[i+1][0])
        if temp < min and piMap[i][1] < piMap[i+1][1] :
            min = temp
    return min

n = 3
price = [5, 10, 3]
print(minimumLoss(price))
