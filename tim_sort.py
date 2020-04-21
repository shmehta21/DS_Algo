# TimSort is the best sorting algo as it has O(n) Time complexity in Best case
# and O(nlogn) complexity in Average and Worst case. Space complexity is O(n)
# Python uses TimSort under the hood when you do a list.sort() or sorted(list) to get the best time complexity


'''
Approach:
1. Establish minRun size (32) and not exceeding (64)
2. Divide the entire array into minRun sizes/chunks and sort the chunks of data
   using insertionSort
3. If chunkSize is not atleast minRun in length, insertionSort grabs subsequent or prior items and 
    inserts them into the chunk until it is minRun size
4. Once all subsections/chunks are sorted , use Merge operation of MergeSort to join the sorted arrays

'''



def insertionSort(array, left, right=None):
	if not right:
		right = len(array)-1

	for i in range(left+1, right+1):
		j = i
		while j > left and array[j-1] > array[j]:
			swap(j-1, j, array)
			j -= 1

	return array

def swap(i, j, array):
	array[i], array[j] = array[j], array[i]

def merge(left, right):
	i = 0
	j = 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1

	while i < len(left):
		result.append(left[i])
		i += 1

	while j < len(right):
		result.append(right[j])
		j += 1

	return result

def timSort(array):
	
    min_run = 32
    n = len(array)

    #create_slices of array as defined by min_run
    # and sort the slices using insertionSort
    for i in range(0, n, min_run):
    	insertionSort(array, i, min((i+min_run-1),n-1))

    # Now start merging the sorted slices/chunks of arrays together into one single array
    size = min_run
    while size < n: #if array length is less than 32, then merge operation does not take place, directly return the array
      for start in range(0, n, size*2):
        midpoint = start + size - 1 #This is where the first slice of the array ends and second one starts
        end = min((start+size*2-1), n-1) # This is where the second slice of the array ends

        merged_array = merge(array[start:midpoint+1], array[midpoint+1:end+1])
        array[start:start + len(merged_array)] = merged_array # Keep copying the sorted and merged arrays in to the actual array at their actual indexes
      size *= 2

    return array
	


if __name__ == '__main__':
	arr1 = list(reversed(range(10)))
	print(timSort(arr1))
	print('-'*100)

	arr2 = list(reversed(range(91)))
	print(timSort(arr2))
	print('-'*100)


	arr3 = list(reversed(range(311)))
	print(timSort(arr3))