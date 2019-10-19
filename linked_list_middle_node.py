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

	
	def traverseList( self ):
		actualNode = self.head
		allElements = []
		while actualNode is not None:
			#print('%d' % actualNode.data)
			allElements.append(actualNode.data)
			actualNode = actualNode.nextNode
			

		return allElements

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

	def findMiddleNode( self ):
		''' Find the middle node of the list 
		by maintaining 2 pointers. Slow will advance
		by 1 position and fast will advance by 2 positions
		'''
		slowPtr = self.head
		fastPtr = self.head
		while fastPtr.nextNode and fastPtr.nextNode.nextNode:
			slowPtr = slowPtr.nextNode
			fastPtr = fastPtr.nextNode.nextNode

		return slowPtr.data

if __name__ == '__main__':
	linkedList = LinkedList()
	linkedList.insertAtPosition(3,0)
	linkedList.insertAtPosition(2,0)
	linkedList.insertAtPosition(1,0)
	size = linkedList.size
	linkedList.insertAtPosition(4, size)
	print('***************************************')
	print(f'Middle node for {linkedList.traverseList()} is {linkedList.findMiddleNode()}')

	linkedList1 = LinkedList()
	linkedList1.insertAtPosition(3,0)
	linkedList1.insertAtPosition(2,0)
	linkedList1.insertAtPosition(1,0)
	size = linkedList1.size
	linkedList1.insertAtPosition(4, size)
	linkedList1.insertAtPosition(5, size)
	print('***************************************')
	print(f'Middle node for {linkedList1.traverseList()} is {linkedList1.findMiddleNode()}')