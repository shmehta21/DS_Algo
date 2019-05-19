######
#Binary search - i/p to binary search is always
#				 a sorted collection of elements. 	
# Big-O complexity is O(logn)			
######



def binary_search( myArr, item ):
	if myArr:
		low  = 0
		high = len(myArr)-1
		count = 0
		while low <= high:
			mid   = int( (low+high)/2 )
			guess = myArr[mid]  #Gets the element from the array index
			if guess == item:
				return mid, count
			elif guess < item:
				count += 1
				low = mid + 1
			elif guess > item:
				count += 1
				high = mid - 1


	else:
		return 'Empty collection cannot be searched'


if __name__ == '__main__':
	result = binary_search([10,15,25,35,55], 15)
	print(result)