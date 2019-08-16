# 
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
########################################################

def maxSubArray( arr ):
	if arr:
		if len(arr)<=1:
			return arr[0]

		currSum = 0
		greatestSum = float('-inf')
		for i in arr:
			if currSum <= 0:
				currSum=i
			else:
				currSum += i

			if currSum>greatestSum:
				greatestSum=currSum
				
		return greatestSum

if __name__ == '__main__':
	arr = [-2,1,-3,4,-1,2,1,-5,4]
	result = maxSubArray(arr)
	print(f'{result}')