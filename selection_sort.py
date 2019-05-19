######
#Selection sort
# Big-O complexity is O(n**2)	
#Selects any one elements as either smallest or biggest(selection) and compares it 
# with rest of the elements		
######

def find_smallest( arr ):
	smallest 	   = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def find_biggest( arr ):
	biggest 	  = arr[0]
	biggest_index = 0
	for i in range(1, len(arr)):
		if arr[i] > biggest:
			biggest = arr[i]
			biggest_index = i
	return biggest_index


def selection_sort_ascending(arr):
	if arr:
		newArr = []
		for i in range(len(arr)):
			smallest = find_smallest(arr)
			newArr.append(arr.pop(smallest))
		return newArr

	else:
		return 'Nothing to sort'

def selection_sort_descending(arr):
	if arr:
		newArr = []
		for i in range(len(arr)):
			biggest = find_biggest(arr)
			newArr.append(arr.pop(biggest))
		return newArr

	else:
		return 'Nothing to sort'
	

if __name__ == '__main__':
	newArr = selection_sort_ascending([5,3,6,2,10])
	print( 'New Arr in ascending order ', newArr )

	newArr1 = selection_sort_descending([5,3,6,2,10])
	print( 'New Arr in descending order ', newArr1 )