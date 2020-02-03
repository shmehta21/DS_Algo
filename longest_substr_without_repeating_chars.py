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
			longest = max(longest, idx-start+1)
		seen[char] = idx
	return longest

if __name__ == '__main__':
	print(f'Longest substring is {lengthOfLongestSubstr("abcabca")}')
	print(f'Longest substring is {lengthOfLongestSubstr("bbbbbb")}')
	print(f'Longest substring is {lengthOfLongestSubstr("abcdefghabc")}')
	print(f'Longest substring is {lengthOfLongestSubstr("sagar")}')
	print(f'Longest substring is {lengthOfLongestSubstr("s")}')
	print(f'Longest substring is {lengthOfLongestSubstr("NaN")}')