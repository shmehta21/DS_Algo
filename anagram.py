###############
# Given a string , check if its anagram of another string
#Meaning: a word formed by rearranging the letters of another, 
#such as spar, formed from rasp.
##############


def is_anagram(str1,str2):
	if len(str1) != len(str2):
		return False

	str1 = sorted(str1)
	str2 = sorted(str2)

	print(f'{str1}, {str2}')

	for i in range(0,len(str1)):
		if str1[i]!=str2[i]:
			return False
	return True

if __name__ == '__main__':
	print(f'Car and Rac are anagrams? -> {is_anagram("Car".upper(),"Rac".upper())}')
	print(f'Roast and Toast are anagrams? -> {is_anagram("Roast".upper(),"Toast".upper())}')
	print(f'nayan and yanna are anagrams? -> {is_anagram("nayan".upper(),"yanna".upper())}')

