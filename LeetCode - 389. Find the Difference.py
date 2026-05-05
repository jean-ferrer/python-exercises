# 2026-05-04

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        lista = list(t)

        if s == "":
            return t

        for letter in t:
            if letter not in s:
                return letter

        for letter in s:
            lista.remove(letter)
            
        return "".join(lista)