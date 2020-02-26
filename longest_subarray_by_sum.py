'''
Problem statement: Given an array = [1,2,3,4,5,6,7,8,9,10] and target sum = 15
find the longest range in array which sums upto target sum.
Output : [1,5] - elements from index 1(0) to 5(4)

Approach: Start with left and right pointers at 0th index
if sum of range(left,right+1) < sum: Increment right
elif sum of range(left,right+1) > sum: Subtract current left from currSum and increment left by 1
elif sum of range(left,right+1) == sum: Record the range of elements as longest if its bigger than 
										previously stored range 
Perform above steps till right pointer is less than length of array
Return the longest range										

'''

def getLongestSubArrayBySum(arr, targetSum):
	left = 0
	right = 0
	longestRange = [left, right]
	while right < len(arr):
		currSum = 0
		for idx in range(left, right+1):
			currSum += arr[idx]

		#print(f'Current sum is {currSum}')
		if currSum == targetSum:
			if abs(longestRange[1] - longestRange[0]) < abs(right - left):
				#print(f'Current longest range was {longestRange}')
				longestRange[:] = [left, right]
				#print(f'longest range changed to {longestRange}')
			right += 1

		elif currSum > targetSum:
			#print(f'Current sum : {currSum} is greater than target sum: {targetSum}')
			currSum -= arr[left]
			left += 1

		elif currSum < targetSum:
			#print(f'Current sum : {currSum} is lesser than target sum: {targetSum}')
			right += 1

	return longestRange



if __name__ == '__main__':
	print(f'{getLongestSubArrayBySum([1,2,3,4,5,6,7,8,9,10], 15)}')
	print(f'{getLongestSubArrayBySum([1,2,3,4,5,0,0,0,9,10], 15)}')
	print(f'{getLongestSubArrayBySum([1,2,3,7,5], 12)}')