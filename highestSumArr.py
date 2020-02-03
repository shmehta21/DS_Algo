traversedIndex = []
def arrayTrip(arr, k):
    if arr:#[0, -3, -2, -5, -7, 1], 3
        highestSum = arr[0]
        for ele in range(1,len(arr)):
            if ele in traversedIndex:
                continue
            if arr[ele] < 0:
                biggestNum = getBiggestNum(ele, arr, k)
                highestSum = highestSum + biggestNum
            else:
                highestSum = highestSum + arr[ele]
        return highestSum

def getBiggestNum(ele, arr, k):
    allNumsUptoK = [arr[ele]]
    
    for i in range(1,k):
        if ele+i < len(arr):
            num = arr[ele+i]
            allNumsUptoK.append( num )
            traversedIndex.append(arr.index(num)) 
    maxNum = max(allNumsUptoK)
    return maxNum
    
if __name__ == '__main__':
    num = arrayTrip([-1, -2, -3], 2) #o/P;-4
    print(num)