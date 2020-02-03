######################################################
#MergeSort - DivideAndConquer 
#Divides array into half and left side contains half array and 
#right side contains the other half. This process repeats till
#we are left with single element arrays.

#These single element arrays are then sorted to form the original array
# Big-O complexity is O(nlogn)			
#####################################################

def merge( left, right ):
	result = []
	i, j = 0, 0
	while i<len(left) and j<len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):# While iterating left and right arrays if one of those arrays gets exhausted, we put remaining elements in the result array
		result.append(left[i])
		i += 1
		
	while j < len(right):
		result.append(right[j])
		j += 1
		
	return result

def mergesort( lst ):
	if len(lst) <= 1: #Base recursive case
		return lst

	mid = int(len(lst)/2)
	left = mergesort(lst[:mid])
	right = mergesort(lst[mid:])
	return merge( left, right )

if __name__ == '__main__':
	
	print(f'Sorted array--> {mergesort([3,9,1,2,34,76,12,97,67])}')

	print(f'Sorted array with 2 elements--> {mergesort([3,9])}')

	print(f'Sorted array with 1 element--> {mergesort([3])}')







