'''
Given an integer array find the first duplicate number

Input: [1,2,1,2,3,3], Output:1
Input: [2,1,3,5,3,2], Output:3 , because the second occurence of 3 is before 2 
Input: [1,2,3,4,5,6], Output:-1 , because there are no dupes
Also, raise exception if below condition is not met

Values in array have to be between 1 and the length of the array
Input: [0,12,15,-1], Output: Invalid array as values in array are not between 1 and length of array
'''

def getFirstDuplicateNumber(inputArr):
	if isValidInputArr(inputArr):
		seen = set()
		firstDupe = None
		for i in inputArr:
			if i not in seen:
				seen.add(i)
			else:
				firstDupe = i
				break
		return firstDupe if firstDupe else -1

		
def isValidInputArr(inputArr):
	isValid = True
	if inputArr:
		lenOfArray = len(inputArr)
		for i in range(lenOfArray):
			if inputArr[i] == 0 or inputArr[i] > lenOfArray:
				isValid = False
				break
	else:
		isValid = False

	if not isValid:
		raise Exception('Input Array is either empty or the elements are not between 1 and length of array')

	return isValid

if __name__ == '__main__':
	print(f'{getFirstDuplicateNumber([1,2,1,2,3,3])}')
	print(f'{getFirstDuplicateNumber([2,1,3,5,3,2])}')
	print(f'{getFirstDuplicateNumber([1,2,3,4,5,6])}')
	#Exception cases of invalid array
	#print(f'{getFirstDuplicateNumber([0,12,15,-1])}')
	#print(f'{getFirstDuplicateNumber([])}')
	#print(f'{getFirstDuplicateNumber([0])}')