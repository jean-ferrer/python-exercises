# 2026-04-29

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dictionary = {}

        for i in range(len(s)):
            char_s = s[i]
            if char_s not in dictionary:
                if t[i] in dictionary.values():
                    return False
                dictionary[char_s] = t[i]
            else:
                if dictionary[char_s] != t[i]:
                    return False
        return True