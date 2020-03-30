'''
Input: arr = [1,2,3,4]
Output: arr = [24,12,8,6]

'''


'''
def productArray(arr):
	if arr:
		if len(arr) == 1:
			return arr
		left = arr[:]
		right = arr[:]
		l = len(arr)
		left[0] = 1
		right[l-1] = 1
		result = []
		for i in range(1, len(left)):
			left[i] = left[i-1] * arr[i-1]
		for j in range(len(arr)-2,-1,-1):
			right[j] = right[j+1] * arr[j+1]

		for idx in range(len(arr)):
			result.append(left[idx]*right[idx])

		return result

if __name__ == '__main__':
	print(f'{productArray([1,2,3,4])}')
'''

'''
input :[7,1,5,3,6,4]	
Get max profit out of buying and selling a stock.
Arr represents prices of a stock on ith day
note: U cannot sell a stock before first buying it
'''
'''
def maxProfitInOneTransaction(priceArr):
	minBuyPrice = min(priceArr)
	idx = priceArr.index(minBuyPrice)
	maxSellPrice = 0
	for price in range(idx, len(priceArr)):
		maxSellPrice = max(priceArr[price], maxSellPrice)


	return maxSellPrice - minBuyPrice

	#Below change for calculating max profit out of multiple buy-sell transactions
	#return sum([max(priceArr[i] - priceArr[i-1],0) for i in range(1,len(priceArr))])

if __name__ == '__main__':
	print(f'{maxProfitInOneTransaction([7,1,5,3,6,4])}') # Buy at 1 and sell at 6
	print(f'{maxProfitInOneTransaction([7,6,4,3,1])}') #In this case profit is not possible, so return 0
'''

def fourNumberSum(arr,tSum):
	quads = []
	allPairs = {}
	for i in range(1, len(arr)-1):
		for j in range(i+1, len(arr)):
			cSum = arr[i] + arr[j]
			diff = tSum - cSum
			if diff in allPairs:
				for pair in allPairs[diff]:
					quads.append(pair + [arr[i], arr[j]])
				
		for k in range(0,i):
			cSum = arr[i] + arr[k]
			if cSum not in allPairs:
				allPairs[cSum] = [[arr[i], arr[k]]]
			else:
				allPairs[cSum].append([arr[i], arr[k]])
	return quads

if __name__ == '__main__':
	print(f'{fourNumberSum([7,6,4,-1,1,2],16)}')