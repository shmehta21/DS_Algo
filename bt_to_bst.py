''' 
1.) Create an array after In-order traversal
2.) Sort the in-order traversal array
3.) Iterate over the in-order array and sorted in-order array together
    and replace elements from sorted_arr to in_order arrat

'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None




def bt_to_bst(root):
	inorder_arr = []
	inorder_traversal(root, inorder_arr)
	sorted_arr = sorted(inorder_arr)

	print(f'Sorted arr => {sorted_arr}')
	for i in range(len(sorted_arr)):
		inorder_arr[i] = sorted_arr[i]

	print(inorder_arr)


def inorder_traversal(root,inorder_arr):
	
	if root.left:
		inorder_traversal(root.left,inorder_arr)

	inorder_arr.append(root.data)

	if root.right:
		inorder_traversal(root.right, inorder_arr)

	print(f'In order arr => {inorder_arr}')
	return inorder_arr

if __name__ == "__main__":
	root = Node(0) 
	root.left = Node(1) 
	root.right = Node(2) 
	root.left.left = Node(3) 
	root.left.right = Node(4)
	root.left.left.right = Node(6)
	root.left.left.right.right = Node(8)
	root.right.left = Node(5) 
	root.right.left.right = Node(7) 

	bt_to_bst(root)