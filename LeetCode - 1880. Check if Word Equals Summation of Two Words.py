# 2026-06-03

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        mapping = {"a": '0', "b": '1', "c": '2', "d": '3', "e": '4', "f": '5', "g": '6', "h": '7', "i": '8', "j": '9'}

        def letter_to_number(word):
            integer = ''
            for letter in word:
                integer += mapping[letter]
            return int(integer)

        if (letter_to_number(firstWord) + letter_to_number(secondWord)) == letter_to_number(targetWord):
            return True
        else:
            return False