# 2026-04-25

class Solution:
    def reverseBits(self, n: int) -> int:
        
        binary = str(bin(n))[2:].zfill(32)
        reversed_binary = binary[::-1]
        integer = int(reversed_binary, 2)

        return integer