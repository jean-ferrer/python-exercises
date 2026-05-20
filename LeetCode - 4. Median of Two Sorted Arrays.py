# 2026-05-20

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        lista = sorted(nums1 + nums2)
        size = len(lista)

        if size % 2 != 0:
            return lista[size//2]
        else:
            return ((lista[size//2] + lista[size//2-1]) / 2)