###########################
# Remove duplicates from a sorted array in-place and return new length
# In-place- Cannot extra place for another array and should be
# done using the same input array without using an auxilliary data structure
# Eg: Given nums = [1,1,2],
#Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#############################


def remove_dupes(nums):
	next_ = 0  #index where unique element must be stored

	for i in range(len(nums)):
		if i == 0 or nums[i] != nums[i-1]:
			nums[next_] = nums[i]
			next_ += 1

	return next_

if __name__ == '__main__':
	result = remove_dupes([0,0,1,1,1,2,2,3,3,4])
	print(f'{result}')