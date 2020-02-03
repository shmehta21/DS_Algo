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

#Time->O(n**2), Space->O(1)
def selectionSortInPlace(arr):
	if arr:
		current_index = 0
		while current_index < len(arr)-1:
			smallest_index = current_index
			for i in range(current_index+1, len(arr)):
				if arr[smallest_index] >  arr[i]:
					smallest_index = i
			swap(current_index, smallest_index, arr)
			current_index += 1
		return arr

def swap(currIdx, smallestIdx, arr):
	arr[currIdx], arr[smallestIdx] = arr[smallestIdx], arr[currIdx]
	

if __name__ == '__main__':
	newArr = selection_sort_ascending([5,3,6,2,10])
	print( 'New Arr in ascending order ', newArr )

	newArr1 = selection_sort_descending([5,3,6,2,10])
	print( 'New Arr in descending order ', newArr1 )

	print(f'Selection sort in place->{selectionSortInPlace([5,3,6,2,10])}')