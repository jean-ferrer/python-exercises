# 2024-12-06

class Solution(object):
    def largestAltitude(self, gain):
        
        current_netgain = 0
        max_netgain = 0

        for e in gain:
            current_netgain += e
            max_netgain = max(current_netgain, max_netgain)
        
        return max_netgain