###########################
#Graph Traversal Algo
#Breadth First Search
#O(V+E) -> V = Vertices, E = Edges

#Visits Layer by layer. Traverses root node and then its neighbours and so on
#For BFS always use a queue like data structure as BFS primarily works on FIFO principle
###########################

class Node(object):
	'''Initialized with its name, its neighbours, 
		boolean visited Flag and the Node's parent/predecessor
		'''
	def __init__( self, name ):
		self.name = name
		self.adjacencyList = []
		self.visited = False
		self.predecessor = None

class BreadthFirstSearch(object):
	def bfs(self, startNode):
		queue = []
		queue.append(startNode)
		startNode.visited = True

		while queue:
			actualNode = queue.pop(0)
			print('%s' % actualNode.name)

			for n in actualNode.adjacencyList:
				if not n.visited:
					n.visited = True
					queue.append(n)

if __name__ == "__main__":
	node1 = Node("A")
	node2 = Node("B")
	node3 = Node("C")
	node4 = Node("D")
	node5 = Node("E")
	node6 = Node("F")
	node7 = Node("G")

	node1.adjacencyList.append(node3)
	node1.adjacencyList.append(node2)

	node2.adjacencyList.append(node4)
	node2.adjacencyList.append(node5)

	node3.adjacencyList.append(node6)
	node6.adjacencyList.append(node7)

	bfs = BreadthFirstSearch()
	bfs.bfs(node1)
