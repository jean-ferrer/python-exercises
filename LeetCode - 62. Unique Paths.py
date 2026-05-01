# 2024-12-07

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # solution = (m+n-2)! / ((m-1)! * (n-1)!)

        solution = factorial(m+n-2) / (factorial(m-1) * factorial(n-1))
        return round(solution)

    def factorial(e):
        if n == 0:
            return 1
        result = 1
        for i in range(1, e+1):
            result *= i
        return result