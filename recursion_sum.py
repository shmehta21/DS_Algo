##############################
#Sum of #'s in a list using recursion' - uses a divide-conquer technique to approach the problem
#	 1.) Identifies a base/recursive case
#	 2.) Divides and reduces the problem until it reaches the base case
# a. Works by adding a list of 0 or 1 #'s with rest of the elements in the list as a separate list
# b. Keeps doing this recursively until all elements in the list have been added up together

##############################


def sum_recursive(myArr):
	if len(myArr) < 2:
		return sum( myArr )
	return myArr[0] + sum_recursive(myArr[1:])

if __name__ == '__main__':
	a1 = [2,3,4]
	print('Sum of elements in a1 ->', sum_recursive(a1))

	a2 = [99]
	print('Sum of elements in a2 ->', sum_recursive(a2))

	a3 = [9,7,8,6,5]
	print('Sum of elements in a3 ->', sum_recursive(a3))