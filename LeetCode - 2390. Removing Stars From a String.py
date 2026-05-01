# 2024-12-16

class Solution:
    def removeStars(self, s: str) -> str:
        
        stack = list()

        for i in s:
            if i != '*':
                stack.append(i)
            elif stack:
                stack.pop()
        
        return ''.join(stack)