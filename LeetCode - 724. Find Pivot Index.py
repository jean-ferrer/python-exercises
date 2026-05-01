# 2024-12-13

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftsum = 0
        rightsum = sum(nums)
        
        for i in range(n):
            rightsum -= nums[i]
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
            
        return -1