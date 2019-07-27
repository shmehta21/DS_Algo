#Single linked list

class Node( object ):
	''' Node class with data and pointer to next node '''
	def __init__( self, data ):
		self.data = data
		self.nextNode = None

class LinkedList( object ):
	''' LinkedList class with root node and size parameter'''

	def __init__( self ):
		self.head = None
		self.size = 0


	def insertStart( self, data ):
		''' 
		creates a new node and if the root is still not created,
		assigns the newly created node as the HEAD, else point the new node's next
		to current HEAD and make new node as the HEAD node.
		O(1) complexity
		'''
		self.size += 1
		newNode  = Node( data )

		if not self.head:
			self.head = newNode
		else:
			newNode.nextNode = self.head
			self.head = newNode

	def insertEnd( self, data ):
		'''
		start at the HEAD and traverse till the end of the list,
		till the last node is found. Last node will be the one whose nextNode will be pointing
		to None. Once this is found , insert the new Node there and set newNode.next  as None
		O(n) complexity
		'''
		self.size += 1
		newNode = Node(data)
		actualNode = self.head
		while actualNode.nextNode is not None:
			actualNode = actualNode.nextNode

		actualNode.nextNode = newNode

	def insertAtPosition( self, data, position ):
		''' 
		Insert at any position in the linked list.
		Check the position and insert the nodes accordingly
		'''
		if position == 0:
			self.insertStart( data )
		elif position > self.size:
			print('Index is out of range')
		elif position == self.size:
			self.insertEnd( data )
		else:
			newNode = Node( data )
			current = self.head
			currentPosition = 0
			while True:
				if currentPosition == position:
					previousNode.nextNode = newNode
					newNode.nextNode = current 
					break
				previousNode = current					
				current = current.nextNode
				currentPosition += 1

		
	def remove( self, data ):
		'''
			Keep a pointer to prevNode, as once you find the node to be removed
			prevNode.next will have to point to currentNode.next.
			If head is to be removed make currentHead.nextNode as the new head 
		'''
		if self.head is None:
			return
		self.size -= 1
		currentNode = self.head
		previousNode = None

		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode


	def traverseList( self ):
		actualNode = self.head
		while actualNode is not None:
			print('%d' % actualNode.data)
			actualNode = actualNode.nextNode

	def actualSize( self ):
		''' 
		Traverses the entire linked list each time when asked for size.
		Hence, size is an instance attribute of class LinkedList.
		Time complexity : O(n)
		'''
		actualNode = self.head
		size = 0
		while actualNode is not None:
			size += 1
			actualNode = actualNode.nextNode;
		return size

if __name__ == '__main__':
	linkedList = LinkedList()
	linkedList.insertAtPosition(3,0)
	linkedList.insertAtPosition(2,0)
	linkedList.insertAtPosition(1,0)
	size = linkedList.size
	linkedList.insertAtPosition(4, size)
	linkedList.traverseList()
	print('***************************************')
	linkedList.remove(3)
	linkedList.traverseList()
	print('***************************************')
	linkedList.insertAtPosition(5,2)
	linkedList.traverseList()