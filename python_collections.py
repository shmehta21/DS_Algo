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

if __name__ == '__main__':
	namedtuple_example()