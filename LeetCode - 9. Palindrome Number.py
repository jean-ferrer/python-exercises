# 2026-04-10

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        reverse = str(x)[::-1]

        if str(x) == reverse:
            return True
        else:
            return False