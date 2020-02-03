##############################
#Quicksort - uses a divide-conquer technique to approach the problem
#	 1.) Identifies a base/recursive case
#	 2.) Divides and reduces the problem until it reaches the base case
# a. Works by identifying a pivot element in the array and then shifts all elements < pivot to its left
# b. all elements > pivot to its right. THen recursively applies quicksort on left and right subarrays
# c. Finally concatenates all the sub arrays and produces a sorted array
# Big-O complexity is O(nlogn)			
##############################


def quick_sort( myArr ):
	 if len( myArr ) < 2:
	 	return myArr
	 else:
	   '''
	   pivot = myArr[0]   #Choosing the pivot-> This should be carefully chosen ,else quicksort might end up giving O(n^2) complexity,
	 						# as the length of call stack would increase from O(logn) to O(n)
	   lesser_than_pivot =  [item for item in myArr[1:] if item <= pivot]
	   greater_than_pivot = [item for item in myArr[1:] if item > pivot]
	   return quick_sort( lesser_than_pivot ) + [ pivot ] + quick_sort( greater_than_pivot )
	   '''
	   pivot = 0
	   left  = [ a for a in myArr[1:] if a <= myArr[pivot]]
	   right = [ a for a in myArr[1:] if a > myArr[pivot]]
	   return quick_sort(left) + [myArr[pivot]] + quick_sort(right)
	   


if __name__ == '__main__':
	a1 = [4,5,1,3,7,9,8]
	print(f'Sorted a1 -> {quick_sort( a1 )}')

	a2 = [23,15,65,19,10,5,42,94,33]
	print(f'Sorted a2 -> {quick_sort( a2 )}')

	a3 = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
	print(f'Sorted a3 -> {quick_sort( a3 )}')

	a4 = [1,1,1]
	print(f'Sorted a4 -> {quick_sort( a4 )}')