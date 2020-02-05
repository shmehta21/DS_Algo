'''
Given a string with all small case letters, find the first non-repeating char.
Return '_' if there is no non-repeating char in the input string

Input: 'aaabcccdeeef', Output: 'b'
Input: 'abcbad', Output: 'c'
Input: 'abcabcabc', Output: '_'
'''

#O(n) time
def getFirstNonRepeatingChar(inputStr):
	''' Fill up a dict with total occurences of each char .
		Then iterate again over inputStr and find the first char 
		in inputStr for which the dict has value 1
	'''
	if inputStr:
		char = None
		seen = {}
		for i in inputStr:
			if i in seen:
				seen[i] += 1
			else:
				seen[i] = 1

		for i in inputStr:
			if seen[i] == 1:
				char = i
				break
			else:
				char = '_'
		return char


if __name__ == '__main__':
	print(f'{getFirstNonRepeatingChar("aaabcccdeeef")}')
	print(f'{getFirstNonRepeatingChar("abcbad")}')
	print(f'{getFirstNonRepeatingChar("abcabcabc")}')
	print(f'{getFirstNonRepeatingChar("ssaggar")}')
	print(f'{getFirstNonRepeatingChar("ssaggarr")}')
