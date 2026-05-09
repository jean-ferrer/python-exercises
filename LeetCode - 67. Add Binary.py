# 2026-05-09

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        soma = int(a, 2) + int(b, 2)
        soma_bin = bin(soma)[2:]

        return soma_bin