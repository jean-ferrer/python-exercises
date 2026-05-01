# 2024-12-12

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        hashmap = dict()

        for i in arr:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        
        all_values = hashmap.values()
        hashmap_unique = set(all_values)

        if len(hashmap_unique) < len(all_values):
            return False
        else:
            return True