# Given a string, find the length of longest substring with non-repeating characters
# Input: abcabca , Output: 3 (abc)
# Input: bbbbbb, Output: 1 (b)
# Input: abcdefghabc, Output: 8 (abcdefgh)

def lengthOfLongestSubstr(inputStr):
	seen  = {}
	start = 0
	longest = 0
	for idx, char in enumerate(inputStr):#(0,a),(1,b)
		if char in seen:
			start = seen[char] + 1
		else:
			longest = max(longest, idx-start)
		seen[char] = idx
	return longest + 1

def longestSubstrWithoutDuplication(inputStr):
	seen = {}
	startIdx = 0
	longest = [0,1]
	for idx, char in enumerate(inputStr):
		if char in seen:
			startIdx = max(startIdx, seen[char]+1)
		if longest[1] - longest[0] < idx - startIdx:
			longest = [startIdx, idx]
		seen[char] = idx
	return inputStr[longest[0]:longest[1]+1] if inputStr[longest[0]] != inputStr[longest[1]] \
									else inputStr[longest[0]:longest[1]]

if __name__ == '__main__':
	print(f'Length of Longest substring is {lengthOfLongestSubstr("abcabca")}')
	print(f'Longest substring is {longestSubstrWithoutDuplication("abcabca")}')

	print(f'Length of Longest substring is {lengthOfLongestSubstr("bbbbbb")}')
	print(f'Longest substring is {longestSubstrWithoutDuplication("bbbbbb")}')

	print(f'Length of Longest substring is {lengthOfLongestSubstr("abcdefghabc")}')
	print(f'Longest substring is {longestSubstrWithoutDuplication("abcdefghabc")}')

	print(f'Length of Longest substring is {lengthOfLongestSubstr("sagar")}')
	print(f'Longest substring is {longestSubstrWithoutDuplication("sagar")}')


	print(f'Length of Longest substring is {lengthOfLongestSubstr("NaN")}')
	print(f'Longest substring is {longestSubstrWithoutDuplication("NaN")}')