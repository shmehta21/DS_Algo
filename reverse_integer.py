'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21
'''

def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        x = abs(x)
        reversed = 0
        
        while x != 0:
            reversed = reversed * 10 + x%10
            x //= 10
            
        if reversed > 2**31-1:
            return 0
        return reversed if not neg else -reversed


if __name__ == '__main__':
    num = 425
    result = reverse(num)
    print(result)
