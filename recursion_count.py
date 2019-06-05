##############################
#Sum of #'s in a list using recursion' - uses a divide-conquer technique to approach the problem
#	 1.) Identifies a base/recursive case
#	 2.) Divides and reduces the problem until it reaches the base case
# a. Works by counting elements in a list of 0 or 1 elements with rest of the elements in a separate list
# b. Keeps doing this recursively until all elements in the list have been counted

##############################

def recursive_count(myArr):
	if len(myArr)<2:
		return len(myArr)
	return len([myArr[0]]) + recursive_count(myArr[1:])

if __name__ == '__main__':
	a = [1,2,3,4,5]
	print('# of elements in a->', recursive_count(a))

	a1 = [1]
	print('# of elements in a1->', recursive_count(a1))