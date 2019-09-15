#Double Linked list

class Node(object):
	def __init__( self, data ):
		self.data = data
		self.prev = None
		self.next = None

class DoubleLinkedList(object):
	def __init__( self ):
		self.size = 0
		self.head = None
		self.tail = None


	def insertStart( self, data ):
		currentNode = self.head
		self.size += 1
		newNode = Node(data)
		if not currentNode:
			self.head = self.tail = newNode
		else:
			newNode.prev = None
			newNode.next = currentNode
			currentNode.prev = newNode
			self.head    = newNode

	def insertEnd( self, data ):
		currentNode = self.head
		self.size += 1
		newNode = Node(data)
		while currentNode.next != None:
			currentNode = currentNode.next

		currentNode.next = newNode
		newNode.prev = currentNode

	def insertAtPosition( self, data, position ):
		if position < self.size:
			self.currPos = 0
			self.size += 1
			currNode = self.head
			newNode = Node(data)
			print(f'Position->{position}, Data->{data}, Size->{self.size}, CurrPos->{self.currPos}')
			if position == 0:
				self.insertStart(data)
			elif position > self.size:
				print('In here')
				self.insertEnd(data)
			else:
				while True and currNode:
					if self.currPos == position:
						newNode.next = prevNode.next
						newNode.prev = prevNode
						prevNode.next.prev = newNode
						prevNode.next = newNode

					prevNode = currNode
					currNode = currNode.next
					self.currPos += 1

	def remove(self, data):
		currentNode = self.head
		if not currentNode:
			return
		self.size -= 1
		prevNode = None
		while currentNode.data != data:
			prevNode = currentNode
			currentNode = currentNode.next
		if not prevNode:
			self.head = currentNode.next
		else:
			prevNode.next = currentNode.next
			currentNode.next.prev = prevNode
			

	def traverseList( self ):
		currentNode = self.head
		while currentNode:
			print(f'{currentNode.data}')
			currentNode = currentNode.next


if __name__ == '__main__':
	dl = DoubleLinkedList()
	dl.insertStart(1)
	dl.insertStart(2)
	dl.insertStart(3)
	dl.insertEnd(4)
	dl.insertEnd(5)
	dl.insertStart(6)
	dl.insertStart(7)
	dl.insertEnd(8)
	dl.insertEnd(9)
	dl.insertAtPosition(10,3)
	dl.traverseList()

	print(f'Size of the doubly linked list is {dl.size} and the head is {dl.head.data}')
	dl.insertAtPosition(11,0)
	dl.traverseList()
	print(f'Size of the doubly linked list is {dl.size} and the new head is {dl.head.data}')
	dl.remove(4)
	dl.traverseList()
	print(f'Size of the doubly linked list after removal is {dl.size} and the new head is {dl.head.data}')
	dl.remove(11)
	dl.traverseList()
	print(f'Size of the doubly linked list after removing the HEAD is {dl.size} and the new head is {dl.head.data}')
