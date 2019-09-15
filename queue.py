# Queue using Python lists -> FIFO

class MyQueue(object):

	def __init__(self):
		self.myQueue = []
	
	def __repr__(self):
		return f'MyQueue({self.myQueue})'

	def enqueue(self,data):
		self.myQueue.append(data)

	def dequeue(self):
		item = self.myQueue[0] #FIFO
		del self.myQueue[0]
		return item

	def peek(self):
		return self.myQueue[0]

if __name__ == '__main__':
	q1 = MyQueue()
	q1.enqueue(1)
	q1.enqueue('A')
	q1.enqueue(2)
	q1.enqueue('B')

	print(f'Queue after enqueueing all items looks like {q1}')

	print(f'Popping from the queue gives {q1.dequeue()}')
	print(f'Popping from the queue gives {q1.dequeue()}')
	print(f'Peeking into the queue returns {q1.peek()}')

	print(f'Queue after dequeueing certain items looks like {q1}')

