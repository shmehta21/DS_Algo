'''
Given an array => [1,2,3,4], return the product at each index of the array,
considering all the remaining elements of the array
Solution => [24,12,8,6]

Approach: Calculate all products to the left of an element till end of array
          Calculate all products to the right of an element till end of array
          Multiply each element of left with respective element from right array

'''

def getArrayProduct(arr):
	left = arr[:]
	right = arr[:]
	l = len(arr)
	left[0] = 1
	right[l-1] = 1
	result = []
	for i in range(1, len(arr)):
		left[i] = arr[i-1] * left[i-1]

	for j in range(len(arr)-2, -1, -1):
		right[j] = arr[j+1] * right[j+1]

	print(f'Left array => {left}')
	print(f'Right array => {right}')

	for idx in range(len(left)):
		result.append( left[idx] * right[idx] )

	return result


if __name__ == '__main__':
	print(f'{getArrayProduct([1,2,3,4])}')
	print(f'==============================')
	print(f'{getArrayProduct([4,3,2,1])}')
	print(f'==============================')
	print(f'{getArrayProduct([7,8,6,5])}')
	print(f'==============================')
	print(f'{getArrayProduct([1])}')