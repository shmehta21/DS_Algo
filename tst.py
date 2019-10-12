#Ternary search tree
#This is similar to Trie but each node only has 3 children (left,middle and right).In this sense it is much better than 
# a Trie as it saves space due to the limited # of references from each node.
# This Data structure can be used for implementing auto-complete/type-ahead kind of functionalities.
# It outperforms HashMap/dict as it just needs the first char to determine if the key is present on not
# whereas a dict needs to compute the hash of the entire key to find out if the key exists.

class Node(object):
	def __init__(self, character):
		self.character = character
		self.value = 0
		self.leftChild = None
		self.rightChild = None
		self.middleChild = None

class TST(object):
	def __init__(self):
		self.root = None

	def put(self,key,value):
		self.root = self.putItem(self.root, key, value, 0)

	def putItem(self, node, key, value, index):
		c = key[index] #take the 0th character while putting a new key 

		if node == None:
			node = Node(c)

		if c < node.character:
			node.leftChild = self.putItem(node.leftChild, key, value, index)
		elif c > node.character:
			node.rightChild = self.putItem(node.rightChild, key, value, index)	
		elif index < len(key) - 1: #index is still smaller than the len of the key and c == node.character
		    node.middleChild = self.putItem(node.middleChild, key, value, index+1)
		else: # last char of the key/str on which we need to set the value
			node.value = value

		return node

	def get(self, key):
		node = self.getItem(self.root, key, 0)

		if node == None:
			return -1
		return node.value

	def getItem(self, node, key, index):

		if node == None:
			return None

		c = key[index]

		if c < node.character:
			return self.getItem(node.leftChild, key, index )
		elif c > node.character:
			return self.getItem(node.rightChild, key, index )
		elif index < len(key)-1:
			return self.getItem(node.middleChild, key, index + 1)
		else:
			return node


if __name__ == '__main__':
	t = TST()
	t.put("adam",100)
	t.put("eva",200)	
	t.put("steve",300)
	t.put("neil",65)

	print(t.get("adam"))
	print(t.get("neil"))
	print(t.get("nail"))
	print(t.get("tail"))

	t.put("cat",20)
	t.put("carrot",30)
	t.put("camel",40)

	print(t.get("cat"))
	print(t.get("carrot"))
	print(t.get("camel"))
	print(t.get("camell"))
