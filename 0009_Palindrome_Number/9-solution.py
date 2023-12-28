class Solution:

    # Solution 1: Convert to string
    def isPalindrome(self, x: int) -> bool:
        # convert to string, then reverse it
        x_str = str(x)
        x_rev = x_str[::-1]
        # compare the original string and the reversed string
        if x_str == x_rev:
            return True
        else:
            return False
            
    # Solution 2: Reverse integer    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            # pop the last digit，and add it to the back of reversed_num，then remove the last digit
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return reversed_num == x