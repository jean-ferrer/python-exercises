# 2026-04-11

class Solution:
    def romanToInt(self, s: str) -> int:
        
        numbers = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        lista = []
        prev = 0
        soma = 0

        for i in s:
            lista.append(numbers[i])
        
        for number in lista:
            if number > prev:
                soma -= prev
            else:
                soma += prev
            prev = number
        
        return soma + number