# 2026-05-19

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])