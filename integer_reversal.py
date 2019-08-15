###############
# Given a # 4321, reverse it and o/p:1234
###############


def reverseInteger(intg):
	if intg:
		strIntg = str(intg)
		newIntg = ''.join(strIntg[::-1])
	return int(newIntg)



if __name__ == '__main__':
	print(f'Reverse of the integer 4321 is {reverseInteger(4321)}')

	print(f'Reverse of the integer 987654321 is {reverseInteger(987654321)}')