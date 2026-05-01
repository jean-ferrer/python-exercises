# 2026-04-14

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        elif x == 1:
            return 1

        sqr = 0

        while sqr*sqr <= x:
            sqr += 1

        return sqr-1