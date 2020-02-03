'''
Write a function that takes an array of unique integers and returns an array
of permutations of those integers. If the input array is empty, your function
should return an empty array
Sample input : [1,2,3]
Sample output : [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

'''
'''
def getPermutations(array):
	permutations = []
	permutationHelper(0, array, permutations)
	return permutations

def permutationHelper(currIdx, array, permutations):
	
	if currIdx == len(array) - 1:
		print(f'Curr index is {currIdx} and array is {array}')
		permutations.append(array[:])
	else:
		for j in range( currIdx,len(array) ):
			print(f'Curr index is {currIdx} and j is {j}')
			swap(array, currIdx, j)
			print(f'Array after first swap is {array}')
			permutationHelper(currIdx+1, array,permutations)#currIdx=2
			print(f'Before swapping 2nd time, currIdx is {currIdx} and j is {j}')
			swap(array, currIdx, j)
			print(f'Array after second swap is {array}')


def swap(array,i,j):
	array[i], array[j] = array[j], array[i]
'''

def getPermutations(array):
	permutations = []
	permutationsHelper(array, permutations, currentPermutation = [])
	return permutations

def permutationsHelper(array, permutations, currentPermutation):
	if not len(array) and len(currentPermutation):
		permutations.append(currentPermutation)
	else:
		for i in range(len(array)):
			newArray = array[:i] + array[i+1:]
			print(f'New array is {newArray}')
			newPermutation = currentPermutation + [array[i]]
			print(f'New permutation is {newPermutation}')
			permutationsHelper(newArray, permutations, newPermutation)


if __name__ == "__main__":
	permutations = getPermutations([1,2,3])
	print(f'All permutations -- {permutations}')