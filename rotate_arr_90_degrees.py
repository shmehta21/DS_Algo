'''
1. Given a n*n array where no.of rows will always be equal to no. of columns,
rotate it by 90 degrees

Eg : Input = [
			  [1  2  3],
			  [4  5  6],
			  [7  8  9]
			 ]

	 Output = [
               [7 4 1],
               [8 5 2],
			   [3 6 9]
	          ]

Approach:
2.Do the following:
    a. Create a transpose of input array 
    b. Start a horizontal swap on the column until you reach len(arr)//2 i.e. center of arr
    

'''


def rotate_90(arr):
	if arr:
		transpose(arr)
		rotate_horizontal(arr)

	return arr

def transpose(arr):
	for i in range(len(arr)):
		for j in range(i,len(arr)):
			swap_while_transpose(i,j,arr)
	

def rotate_horizontal(arr):
	print(f'arr b4 horizontal rotate == {arr}')
	for i in range(len(arr)):
		for j in range(0, len(arr)//2):
			swap_while_rotate(i, j, arr)
	

def swap_while_transpose(i, j, arr):
	i_j = arr[i][j]
	j_i = arr[j][i]
	arr[i][j] = j_i
	arr[j][i] = i_j

def swap_while_rotate(i, j, arr):
	i_j = arr[i][j]
	arr[i][j] = arr[i][len(arr)-1-j]
	arr[i][len(arr)-1-j] = i_j
	



if __name__ == '__main__':
	input_1 = [[1,2,3],[4,5,6],[7,8,9]]
	rotated_arr = rotate_90(input_1)
	print(rotated_arr, end='\n')

	input_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	rotated_arr = rotate_90(input_2)
	print(rotated_arr, end='\n')