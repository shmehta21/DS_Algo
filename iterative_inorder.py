'''
Iterative In order:
1. Create an empty stack
2. Initialize current node = root
3. Push root to stack and set current = current.left until current is NULL
4. If current is NULL and stack is not empty
      a. Pop item from stack and print it
      b. Set current = popped_item.right
      c. Go to step 3
5. Current is NULL and stack is empty. We are DONE

'''

class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None

def inOrder(root):
	current = root
	stack = []
	while True:
		if current:
			stack.append(current)
			current = current.left

		elif stack:
			current = stack.pop()
			print(current.data)
			current = current.right

		else:
			break


if __name__ == '__main__':
	root = Node(1) 
	root.left = Node(2) 
	root.right = Node(3) 
	root.left.left = Node(4) 
	root.left.right = Node(5) 
  
	print(f'{ inOrder(root) }')
