# 2024-12-04

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        maxcandies = max(candies)

        for kid in candies:
            kidpluscandies = kid + extraCandies 
            if kidpluscandies >= maxcandies:
                result.append(True)
            else:
                result.append(False)

        return result