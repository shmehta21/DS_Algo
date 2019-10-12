
#Compare 2 binary trees in terms of their topology and values in each node
class Node(object):
	def __init__(self, data):
		self.data = data
		self.leftChild = None
		self.rightChild = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None

	def insert(self, data):
		if not self.root:
			self.root = Node(data)
		else:
			self.insertNode(self.root, data)

	def insertNode(self, node, data):
		if data < node.data:
			if node.leftChild:
				self.insertNode(node.leftChild, data)
			else:
				node.leftChild = Node(data)

		elif data > node.data:
			if node.rightChild:
				self.insertNode(node.rightChild, data)
			else:
				node.rightChild = Node(data)

class TreeComparator(object):
	def compare_trees(self, node1, node2):
		#Recursive base case
		#If we are comparing the leaf Node , both its children(left and right) would be None . 
		#So this check would perform None == None , which should return True
		if not node1 or not node2: 
		    return node1==node2

		if node1.data != node2.data: #Data check
		    return False

		#Topology and Data checks - recursive
		return self.compare_trees(node1.leftChild, node2.leftChild) and self.compare_trees(node1.rightChild, node2.rightChild)


if __name__ == '__main__':
	bst_one = BinarySearchTree()
	bst_one.insert(10)
	bst_one.insert(13)
	bst_one.insert(2)
	bst_one.insert(14)

	bst_two = BinarySearchTree()
	bst_two.insert(10)
	bst_two.insert(13)
	bst_two.insert(2)
	bst_two.insert(14)

	comp = TreeComparator()
	print(f'Are bst_one and bst_two equal? {comp.compare_trees(bst_one.root, bst_two.root)}')

	bst_three = BinarySearchTree()
	bst_three.insert(5)

	bst_four = BinarySearchTree()
	bst_four.insert(6)
	print(f'Are bst_three and bst_four equal? {comp.compare_trees(bst_three.root, bst_four.root)}')

	bst_five = BinarySearchTree()
	bst_five.insert(10)
	bst_five.insert(2)
	bst_five.insert(13)
	bst_five.insert(14)

	bst_six = BinarySearchTree()
	bst_six.insert(10)
	bst_six.insert(13)
	bst_six.insert(5)
	bst_six.insert(14)
	print(f'Are bst_five and bst_six equal? {comp.compare_trees(bst_five.root, bst_six.root)}')

	bst_seven = BinarySearchTree()
	bst_seven.insert(10)
	bst_seven.insert(5)
	bst_seven.insert(13)
	bst_seven.insert(14)

	bst_eight = BinarySearchTree()
	bst_eight.insert(10)
	bst_eight.insert(13)
	bst_eight.insert(5)
	bst_eight.insert(14)
	print(f'Are bst_seven and bst_eight equal? {comp.compare_trees(bst_seven.root, bst_eight.root)}')


