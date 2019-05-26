######################################
#Python collections package:
#Counter
#OrderedDict
#namedtuple
#deque
#defaultdict
#####################################

def namedtuple_example():
	from collections import namedtuple

	Car = namedtuple('Car','Make Model Year')
	c1  = Car('Nexa','Baleno', '2015')
	c2  = Car('Honda','Accord', '2005')
	#Car objects are now immutable
	
	iter_  = ['Audi','Q4', '2005']
	another_iter = ['BMW','Mercedez_Benz','1995']

	#Access items by attribute
	print('Car details by attribute-->', c1.Make, c1.Model, c1.Year )

	#Access items by position
	print('Car details by position-->', c2[0], c2[1], c2[2] )

	#Initializing Car from a sequence/iterable
	c3 = Car(*iter_)
	print('Car details initialized from an iterable-->', c3.Make, c3.Model, c3.Year)

	c4 = Car._make(another_iter)
	print('Car details initialized from another iterable-->', c4.Make, c4.Model, c4.Year)

#Use of Deque already covered in palindrome_checker_deque.py
def deque_example():
	pass

def counter_example():
	from collections import Counter
	#Counter extends from dict, stores  elements as keys and its count as values
	c=Counter('abcdseefadhasfdjlfdleadfdsafsfdfgwwerewre')

	#Unique elements of Counter
	print('Elements of the counter->', set(c.elements()))

	#3 most common elements of the Counter
	print('3 most common elements of the counter->', c.most_common(3))

	# n least common elements, n=3 for this example
	#subtract n from -1, if we dont, then we get -1 and -2 which is the first 2 least common instead of 3 least common
	print('n least common elements->', c.most_common()[:-3-1:-1]  )

	#Get the count of all elements in the Counter
	print('Count of all elements in the counter->', c.items())

	#Total count of all occurences of elements in the Counter
	print('3 most common elements of the counter->', sum(c.values()))

def orderedDict_example():
	pass

def defaultDict_example():
	from collections import defaultdict
		

if __name__ == '__main__':
	namedtuple_example()
	counter_example()
	orderedDict_example()
	defaultDict_example()