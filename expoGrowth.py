def exponentialGrowth(arr, n):
	sortedArr = sorted(arr)
	for i in range(len(sortedArr)):
		print(f' i is {i} and arr[i] is {sortedArr[i]} ')
		if sortedArr[i] == n:
			sortedArr[i] = sortedArr[i] * 2
			n = sortedArr[i]
			print(f'n is {n}')
	return n

if __name__ == '__main__':
    num = exponentialGrowth([8, 7, 6, 5, 4, 3, 2, 1], 3)
    print(num)