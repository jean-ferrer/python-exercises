# 2026-04-16

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        binary = bin(n)
        counter = 0

        for i in binary:
            if i == "1":
                counter += 1
        
        return counter