####################
#Binary serch tree
#Keeps the keys in sorted order so we can skip half the tree while looking up keys
#Every node can have atmost 2 children
# Items in left tree/subtree will be lesser than root
# Items in right tree/subtree will be greater than the root

#All operations are performed with O(log N) time complexity, provided the tree is balanced
#If the BST becomes unbalanced, time complexity reduces to O(n)

#Height-> # of layers determine the height of BST. IF height is 'h' , total # of nodes a BST can contain would be 2^(h-1).
# So a BST with height 4 can have atmost 2^3 = 8 nodes



#Traversals in Recursive Order
#1. InOrder = Left, Root, Right
#2. PreOrder = Root, Left, Right
#3. PostOrder = Left, Right, Root
####################

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
			self.insertNode( data, self.root )

	def insertNode( self, data, node):
		''' Running time for insertion is O(logn)
			if tree is balanced, else it can be reduced to O(n)
		'''
		if data < node.data:
			if node.leftChild:
				self.insertNode( data, node.leftChild )#If left child already exists than go further down the tree to the left
			else:
				node.leftChild = Node(data)
		else:
			if node.rightChild:
				self.insertNode( data, node.rightChild )#If right child already exists than go further down the tree to the right
			else:
				node.rightChild = Node(data)

	def removeNode(self, data, node):
		if not node:
			return node

		if data < node.data:
			node.leftChild = self.removeNode( data, node.leftChild )
		elif data > node.data:
			node.rightChild = self.removeNode( data, node.rightChild )
		else: #this is the case where data == rootNode.data
			  #rootNode can be leaf node OR it could have either left/right child only OR it could have both left and right child
			if not node.leftChild and not node.rightChild: #removing a leaf node
				print('Removing a leaf node')
				del node
				return None

			if not node.leftChild:
				print('Removing a node with single right child...')
				tempNode = node.rightChild
				del node
				return tempNode
			elif not node.rightChild:
				print('Removing a node with single left child...')
				tempNode = node.leftChild
				del node
				return tempNode

			print('Removing node with 2 children...')
			tempNode = self.getPredecessor(node.leftChild)#get the greatest element from left subtree OR get the smallest item from right subtree and swap it with root node
			node.data = tempNode.data
			node.leftChild = self.removeNode(tempNode.data, node.leftChild) #once swapped woth root node remove that particular left child

		return node

	def getPredecessor( self, node):
		if node.rightChild:
			return self.getPredecessor(node.rightChild)

		return node

	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data,self.root)

	def getMinValue( self ):
		if self.root:
			return self.getMin(self.root)

	def getMin(self, node):
		if node.leftChild:
			return self.getMin(node.leftChild) #Check recursively till u go to the leftmost array as that will be the smallest node

		return node.data

	def getMaxValue( self ):
		if self.root:
			return self.getMax(self.root)

	def getMax(self, node):
		if node.rightChild:
			return self.getMax(node.rightChild) #Check recursively till u go to the rightmost array as that will be the greatest node

		return node.data

	def traverse(self, style):
		if self.root:
			if style == 'InOrder':
				self.traverseInOrder(self.root)
			elif style == 'PreOrder':
				self.traversePreOrder(self.root)
			else:
				self.traversePostOrder(self.root)

	def traverseInOrder(self, node):
		''' InOrder traversal -> Left Root Right'''
		if node.leftChild:
			self.traverseInOrder(node.leftChild)

		print('%s' % node.data)

		if node.rightChild:
			self.traverseInOrder(node.rightChild)

	def traversePreOrder(self, node):
		print('%s' %node.data)

		if node.leftChild:
			self.traversePreOrder( node.leftChild )
		if node.rightChild:
			self.traversePreOrder( node.rightChild )

	def traversePostOrder(self, node):
		if node.leftChild:
			self.traversePostOrder( node.leftChild )
		if node.rightChild:
			self.traversePostOrder( node.rightChild )

		print('%s' % node.data)


if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.insert(10)
	bst.insert(5)
	bst.insert(6)
	bst.insert(15)
	print('Integer BST')
	print(bst.getMinValue())
	print(bst.getMaxValue())
	bst.remove(5)
	print('Result of InOrder traversal for Integer BST')                                                                                      
	bst.traverse(style='InOrder')

	print('Result of PreOrder traversal for Integer BST')                                                                                      
	bst.traverse(style='PreOrder')

	print('Result of PostOrder traversal for Integer BST')                                                                                      
	bst.traverse(style='PostOrder')

	charbst = BinarySearchTree()
	charbst.insert('C')
	charbst.insert('A')
	charbst.insert('Z')
	charbst.insert('G')

	print('Character BST')
	print(charbst.getMinValue())
	print(charbst.getMaxValue())
	charbst.remove('Z')
	print('Result of InOrder traversal for Character BST')                                                                                      
	charbst.traverse(style='InOrder')




