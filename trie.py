# Trie : there is no limit on the number of children each node can have
# Has more mem complexity when compared to Ternary search tree
# in best case this data structure can outperform HashMap/Dict
# as it only checks if the first letter of the word is present or not 
# as one of the children of the root node. Unlike dicts it does not need to compute
# the hash of the entire key to see if the searched key is present in the dict or not.


class Node(object):
	def __init__(self, ch):
		self.ch = ch
		self.children = {}
		self.word_finished = False
		

class Trie(object):
	def __init__(self):
		self.root = Node('*')

	def insert(self, word):
		current = self.root
		print(f'Root node during insertion is {current.ch} and its children are {current.children.keys()}')
		for ch in word:
			if ch in current.children:
				print(f'Satisfied the condition for {ch} in {word}')
				current = current.children[ch]
				#current.counter += 1	
			else:
				newNode = Node(ch)
				current.children[ch] = newNode
				current = newNode
				#current.counter += 1
		current.word_finished = True #As you traverse each char of a word, "current" pointer changes to the next node and finally
									 #when you reach last node current.word_finished will be set to True


	def search(self, word):
		if not self.root.children:
			return False
		current = self.root
		for char in word:
			if char in current.children:
				current = current.children[char]
			else:
				return False
		if current.word_finished: #If end of the word is reached, then last char would have been tagged with word_finished = True
			return True
		return False

if __name__ == '__main__':
	tree = Trie()
	tree.insert('bata')
	tree.insert('hackathon')
	tree.insert('ha')
	tree.insert('hac')
	tree.insert('bat')

	
	print(f"Word hac found? -- {tree.search('hac')}")
	print(f"Word hack found? -- {tree.search('hack')}")
	print(f"Word hackathon found? -- {tree.search('hackathon')}")
	print(f"Word ha found? -- {tree.search('ha')}")
	print(f"Word bata found? -- {tree.search('bata')}")
	