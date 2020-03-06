'''
Given an array of integers, return an array of length 2:
First element should be the greatest sum that can be generated from 
a strictly-increasing subsequence in the input array

Second should be the array of numbers in that subsequence
Eg 1:
Input: [10,70,20,30,50,11,30] 
Output: [110,[10,20,30,50]] 

Eg 2:
Input: [8,12,2,3,15,5,7] 
Output: [35,[8,12,15]] 
'''
def maxIncreasingSubsequence(arr):
	sequences = [None for i in arr]
	newArr = arr[:]
	maxIdx = 0
	for i in range(len(arr)):
		currNum = arr[i]
		for j in range(0,i):
			prevNum = arr[j]
			if prevNum < currNum and newArr[j] + currNum >= newArr[i]:
				newArr[i] = newArr[j] + currNum
				sequences[i] = j
		if newArr[i] > newArr[maxIdx]:
			maxIdx = i
	return [newArr[maxIdx], buildSequence(maxIdx, arr, sequences)]

def buildSequence(maxIdx, arr, sequences):
	seq = []
	while maxIdx is not None:
		seq.append(arr[maxIdx])
		maxIdx = sequences[maxIdx]
	return list(reversed(seq))

if __name__ == "__main__":
	arr = [10,70,20,30,50,11,30]
	print(f'{maxIncreasingSubsequence(arr)}')

	arr_1 = [8,12,2,3,15,5,7]
	print(f'{maxIncreasingSubsequence(arr_1)}')

