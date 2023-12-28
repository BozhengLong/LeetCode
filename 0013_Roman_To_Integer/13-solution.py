class Solution:
    def romanToInt(self, s: str) -> int:
        # use dictionary to store the value of each roman character
        m = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        # ans to store the final result
        ans = 0

        # if the current character is less than the next character, then subtract the current character from the next character
        # else add the current character to the ans
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
                
        return ans