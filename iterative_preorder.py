'''
1. Current Node to be set as root
2.Do the following while stack is not empty:
    a. Pop an item from stack and print it
    b. Push right Child of popped item to stack
    c. Push left Child of popped item to stack

   Right child is pushed first so that left subtree gets processed first

'''

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def iterativePreOrder(root):
	current = root
	stack = []
	stack.append(current)

	while stack:
		current = stack.pop()
		print(current.data)

		if current.right:
			stack.append(current.right)

		if current.left:
			stack.append(current.left)

if __name__ == '__main__':
	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
	
	iterativePreOrder(root) 