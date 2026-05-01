# 2024-12-02

class Solution():
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        self.word1 = word1
        self.word2 = word2

        string = ''

        i = 0
        lenword1 = len(word1)
        lenword2 = len(word2)

        if lenword1 < lenword2:
            minsize = lenword1
            maxsize = lenword2
            case = 1
        elif lenword1 > lenword2:
            minsize = lenword2
            maxsize = lenword1
            case = 2
        else:
            minsize = maxsize = lenword1 = lenword2
            case = 3

        while i < minsize:
            string += word1[i]
            string += word2[i]
            i += 1
        
        while i < maxsize:
            if case == 1:
                string += word2[i]
                i += 1
            elif case == 2:
                string += word1[i]
                i += 1

        return string