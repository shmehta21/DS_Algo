#Bubble sort O(n^2)
#Bubble sort just bubbles the maximum value of the array to the top at the end of each pass,
#Hence arraySize-i in the inner for loops

def bubble_sort(nums):
	if nums:
		arraySize = len(nums)-1
		for i in range(arraySize):
		  for j in range(arraySize-i):#Compare jth element with j+1th element i times where i = arraySize
		  	if nums[j] > nums[j+1]:	  # At every iteration we consider the last element to be sorted, so arraySize-i	
		  		swap(nums,j, j+1)
		return nums

def swap(num, i, j):
	num[i], num[j] = num[j], num[i]

if __name__ == '__main__'	:
	print(f'{bubble_sort([1,5,3,2,4,8,7])}')
	print(f'{bubble_sort([4,3,2,1])}')
	print(f'{bubble_sort([3,4,3,4])}')
	print(f'{bubble_sort([-1,-3,-9,4])}')
	print(f'{bubble_sort([1,1,1,1])}')