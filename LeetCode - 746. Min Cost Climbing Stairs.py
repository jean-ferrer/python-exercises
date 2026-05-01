# 2024-12-08

from typing import List

class Solution:

    def minCostClimbingStairs(self, cost):
        
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        dp = []
        i = 0
        while i < len(cost):
            dp.append(0)
            i += 1
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        i = 2
        while i < len(cost):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            i += 1
        
        return min(dp[-1], dp[-2])