###############
#Deque - pronounced as 'Deck' allows insertion and removal 
#from both sides of the queue

#Rear side is the left one and front side is on the right
#Eg:
#s = deque()
#s.appendleft(1)  --> [1]
#s.appendleft(2)  --> [2,1]
#s.append(3)      --> [2,1,3] 
#s.popleft()      --> [1,3] 
#s.pop( )         --> [1] 
################


from collections import deque

def palindrome_checker( palin_str ):
	palin_checker = deque()

	if palin_str:
		for each_char in palin_str:
			palin_checker.appendleft(each_char)

	are_chars_equal = True
	while len(palin_checker) > 1 and are_chars_equal:
		first_char = palin_checker.popleft()
		last_char  = palin_checker.pop()
		if first_char.lower() != last_char.lower():
			are_chars_equal = False
			break
	return are_chars_equal

if __name__ == '__main__':
	print('Radar is a palindrome? ->', palindrome_checker('radar') )
	print('ldfghysfr is a palindrome? ->', palindrome_checker('ldfghysfr') )
	print('madaM is a palindrome? ->', palindrome_checker('madaM') )