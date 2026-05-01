# 2024-12-03

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        self.n = n
        
        ans = []

        i = 0
        while i < n + 1:

            binary = bin(i)[2:]

            soma = 0

            for _ in binary:
                if _ == '1':
                    soma += 1

            ans.append(soma)

            i += 1
        
        return ans