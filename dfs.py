class Node(object):
	def __init__(self, name):
		self.name = name
		self.visited = False
		self.adjacencyList = []

class DepthFirstSearch(object):
	def dfs(self, startNode):
		startNode.visited = True
		print(f'{startNode.name}')

		for n in startNode.adjacencyList:
			if not n.visited:
				self.dfs(n)

	def dfs_stack(self, startNode):
		stack = []
		stack.append(startNode)
		startNode.visited = True
		while stack:
			actualNode = stack.pop()
			print(f'{actualNode.name}')
			for node in actualNode.adjacencyList:
				if not node.visited:
					node.visited = True
					stack.append(node)


node1 = Node('A')					
node2 = Node('B')					
node3 = Node('C')					
node4 = Node('D')					
node5 = Node('E')					
node6 = Node('F')					
node7 = Node('G')					
node8 = Node('H')					
node9 = Node('I')
node10 = Node('J')

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node6)
node1.adjacencyList.append(node7)
node2.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)
node5.adjacencyList.append(node9)
node5.adjacencyList.append(node10)
node7.adjacencyList.append(node8)

depthFirstSearch = DepthFirstSearch()
depthFirstSearch.dfs(node1)
print('*************************************************')
depthFirstSearch1 = DepthFirstSearch()
depthFirstSearch1.dfs_stack(node1)