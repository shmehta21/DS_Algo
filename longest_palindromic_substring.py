'''
Input string: 'abaxyzzyxf'
Output string: 'xyzzyx'
Explanation:
output string should be part of original string
and the task is to find the longest PALINDROMIC substring
NOTE: The output string is a palindrome as it reads the same from
both sides

'''

def getLongestPalindromicSubstr(inputStr):
	currLongest = [0,1]
	for i in range(1,len(inputStr)):
		odd = getPalindromicStr(inputStr, i-1, i+1)
		even = getPalindromicStr(inputStr, i-1, i)
		longest = max(odd, even, key=lambda x: x[1] - x[0])
		currLongest = max(longest, currLongest, key=lambda x:x[1] - x[0])
	return inputStr[currLongest[0]:currLongest[1]]

def getPalindromicStr(inputStr, left, right):
	while left >= 0 and right < len(inputStr):
		if inputStr[left] != inputStr[right]:
			break
		left -= 1
		right += 1
	return [left+1, right]

if __name__ == '__main__':
	print(f'{getLongestPalindromicSubstr("abaxyzzyxf")}')
	print(f'{getLongestPalindromicSubstr("a")}')
	print(f'{getLongestPalindromicSubstr("abcdzzzzzzzabcd")}')
	print(f'{getLongestPalindromicSubstr("abcdzzzzzzzdcba")}')