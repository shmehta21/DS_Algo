##########################################################
# Djikstra's is a shortest path algorithm that calculates
# the shortest path between two nodes using a greedy approach
# Overall running time is O(VlogV+E)
# We use a priority queue(heap) as we need to get the node 
# with the minimum weight on every iteration. The heap will have root node with weight 0
# and the rest initialized to infinity. If we use any other data structure
# the process of finding the node with shortest weight on every iteration will worsen to O(n)
# With heapq a.k.a the 0th element is always the node with minimum weight
# heapq.heapify operation sorts an unsorted list in a way that the 0th element will show up the lowest value
###########################################################

import sys
import heapq

class Edge(object):
	def __init__( self, weight, startVertex, targetVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.targetVertex = targetVertex

class Node(object):
	def __init__( self, name):
		self.name = name
		self.visited = False
		self.predecessor = None
		self.adjacencyList = [] #neighbours of a node
		self.minDistance = sys.maxsize #initialize the node to max value and then update as you traverse each node
	'''
	def __cmp__( self, otherVertex ):#Decides shortest path for a node based on minimum distance
		return self.cmp( self.minDistance, otherVertex.minDistance )
	'''

	
	def __lt__( self, other ):#Defines how one node is smaller or greater than the other one
		selfPriority = self.minDistance
		otherPriority = other.minDistance
		return selfPriority < otherPriority
	

class Djikstras():
	def __init__(self):
		pass

	def calculateShortestPath(self,startVertex):
		q = []
		startVertex.minDistance = 0
		heapq.heappush(q, startVertex)#Store the heap in a one dimensional array(list in python)

		while len(q) > 0:
			actualVertex = heapq.heappop(q) # return node with min distance as top of the heapq will always have the min element
			for edge in actualVertex.adjacencyList:
				u = edge.startVertex
				v = edge.targetVertex
				newDistance = u.minDistance + edge.weight

				if newDistance < v.minDistance:
					v.predecessor = u
					v.minDistance = newDistance
					heapq.heappush(q,v)#This call refers the overridden __lt__  implementation to compare the smallest element and push it on 0th position on the heapq

	def getShortestPathTo(self, targetVertex):
		print(f'Shortest path to {targetVertex.name} is {targetVertex.minDistance}')
		node = targetVertex
		while node is not None:
			print(f'{node.name}')
			node = node.predecessor


if __name__ == '__main__':
	node1 = Node('A')
	node2 = Node('B')
	node3 = Node('C')
	node4 = Node('D')
	node5 = Node('E')

	edge1 = Edge(3, node1, node2)
	edge2 = Edge(5, node1, node3)
	edge3 = Edge(7, node1, node4)
	edge4 = Edge(6, node2, node3)
	edge5 = Edge(9, node2, node5)
	edge6 = Edge(11,node3, node5)
	edge7 = Edge(13,node3, node4)
	edge8 = Edge(18,node4, node5)

	node1.adjacencyList.append(edge1)
	node1.adjacencyList.append(edge2)
	node1.adjacencyList.append(edge3)
	node2.adjacencyList.append(edge4)
	node2.adjacencyList.append(edge5)
	node3.adjacencyList.append(edge6)
	node3.adjacencyList.append(edge7)
	node4.adjacencyList.append(edge8)

	algorithm = Djikstras()
	algorithm.calculateShortestPath(node1)
	algorithm.getShortestPathTo(node5)


