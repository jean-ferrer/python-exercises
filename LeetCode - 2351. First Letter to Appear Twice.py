# 2026-04-08

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        lista = set()

        for i in s:
            if i not in lista:
                lista.add(i)
            else:
                return i