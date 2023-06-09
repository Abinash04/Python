'''
9.
https://leetcode.com/problems/palindrome-number/
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:

        num = x
        rev = 0
        while x > 0:
            rev = (rev * 10) + x % 10
            x = x // 10
            print('rev:',rev,'x:',x)
        
        print(num, rev)
        if num == rev:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(1331))