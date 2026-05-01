# 2024-12-04

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current = sum(nums[:k])
        maximum = current

        for i in range(k, len(nums)):
            current += nums[i] - nums[i-k]
            maximum = max(maximum, current)

        return maximum / k