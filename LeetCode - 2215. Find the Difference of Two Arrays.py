# 2024-12-03

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        self.nums1 = nums1
        self.nums2 = nums2

        list1 = []
        list2 = []

        for i in nums1:
            if i not in list1:
                list1.append(i)
        for i in nums2:
            if i not in list2:
                list2.append(i)

        answer = []
        part1 = []
        part2 = []

        for i in list1:
            if i not in list2:
                part1.append(i)
        for i in list2:
            if i not in list1:
                part2.append(i)

        answer.append(part1)
        answer.append(part2)

        return answer