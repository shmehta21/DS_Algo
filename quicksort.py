##############################
#Quicksort - uses a divide-conquer technique to approach the problem
#	 1.) Identifies a base/recursive case
#	 2.) Divides and reduces the problem until it reaches the base case
# a. Works by identifying a pivot element in the array and then shifts all elements < pivot to its left
# b. all elements > pivot to its right. THen recursivley applies quicksort on left and right subarrays
# c. Finally concatenates all the sub arrays and produces a sorted array
# Big-O complexity is O(nlogn)			
##############################


def quick_sort( myArr ):
	 if len( myArr ) < 2:
	 	return myArr
	 else:
	   pivot = myArr[0]   #Choosing the pivot-> This should be carefully chosen ,else quicksort might end up giving O(n^2) complexity,
	 						# as the length of call stack would increase from O(logn) to O(n)
	   lesser_than_pivot =  [item for item in myArr[1:] if item < pivot]
	   greater_than_pivot = [item for item in myArr[1:] if item > pivot]
	   return quick_sort( lesser_than_pivot ) + [ pivot ] + quick_sort( greater_than_pivot )

if __name__ == '__main__':
	a1 = [4,5,1,3,7,9,8]
	a1_sorted =quick_sort( a1 )
	print('Sorted a1 ->', a1_sorted)

	a2 = [23,15,65,19,10,5,42,94,33]
	a2_sorted = quick_sort( a2 )
	print('Sorted a2 ->', a2_sorted)

	a3 = [5]
	a3_sorted = quick_sort( a3 )
	print('Sorted a3 ->', a3_sorted)