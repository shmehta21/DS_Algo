#Insertion sort O(n^2)
#Insertion sort just sinks the minimum value from the array to the bottom at the end of each pass,
#At every pass, there is just one swap compared to bubble sort where we make multiple swaps


def insertion_sort(nums):
	for i in range(len(nums)):
	  j=i
	  while j > 0 and nums[j-1] > nums[j]:#Compare jth element with j-1th
	  		swap(nums,j, j-1)
	  		j = j-1
	return nums

def swap(num, i, j):
	num[i], num[j] = num[j], num[i]

if __name__ == '__main__'	:
	print(f'{insertion_sort([1,5,3,2,4,8,7])}')
	print(f'{insertion_sort([4,3,2,1])}')
	print(f'{insertion_sort([3,4,3,4])}')
	print(f'{insertion_sort([-1,-3,-9,4])}')
	print(f'{insertion_sort([1,1,1,1])}')