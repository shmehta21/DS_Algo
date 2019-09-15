# Stack using Python lists -> LIFO

class MyStack( object ):
	def __init__(self):
		self.myStack = []
		self.size = 5

	def __len__(self):
		return len(self.myStack)

	def push(self, data):
		if len(self.myStack) >= self.size: #List can be resized here as an alternate OR we can implement Stack as a linked list so that there is no mem constraint and a linked list will grow dynamically
			print('Stack overflow!!!')
			return

		self.myStack.append(data)

	def pop(self):
		if len(self.myStack) == 0:
			print('Stack underflow!!! No items left on the stack')
			return

		item = self.myStack[-1] #LIFO
		del self.myStack[-1]
		return item

	def peek(self):
		return self.myStack[-1]

if __name__ == '__main__':
	s1 = MyStack()
	s1.push(1)
	s1.push('A')
	s1.push(2)
	s1.push('B')
	print(f'Stack size before popping: {len(s1)}')
	print(f'Peeping last item on stack: {s1.peek()}')
	print(f'Popping out {s1.pop()} from stack')
	print(f'Popping out {s1.pop()} from stack')

	s1.push(3)
	s1.push('C')
	s1.push(4)
	s1.push('D')

	s2 = MyStack()
	s2.pop()




