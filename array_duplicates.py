###############
# Find dupes in a one dimensional array where integer values
# are less than the lenght of the array
# Eg: [2,7,5,1,2,7], o/p: [2].
# Result should not contain 7 as length of array is less than 7
###############

from collections import Counter

def duplicates(nums):
	c = Counter(nums)
	dupeVals = []
	for key, val in c.items():
		if val > 1:
			if key <= len(nums):
				dupeVals.append(key)
	print("Repetition found for vals:", dupeVals)
		

if __name__ == '__main__':
	nums = [2,7,5,1,2,7]
	duplicates(nums)