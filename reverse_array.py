#Reverse an array in place with O(n) complexity
def reverse_array(nums):
	'''
		Maintain a start and end pointer and decrement
		till startIndex < endIndex
		Eg: [1,2,3,4,5] should become [5,4,3,2,1]
	'''
	startIndex = 0
	endIndex   = len(nums)-1

	while startIndex < endIndex:
		#swap items at the index
		nums[startIndex], nums[endIndex] = nums[endIndex], nums[startIndex]

		#increment the start index
		startIndex += 1
		#decrement the end index
		endIndex -= 1

	#the reversed array
	return nums


if __name__ == "__main__":
	nums = [1,2,3,4,5]
	print(f'Reverse of {nums} is {reverse_array(nums)}')