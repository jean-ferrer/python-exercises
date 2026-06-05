# 2026-06-05

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        max_size_list = list()
        index = range(0, len(grid[0]))

        for i in index:
            max_size = 0
            for j in grid:
                number = (str(j[i]))
                if len(number) > max_size:
                    max_size = len(number)
            max_size_list.append(max_size)

        return max_size_list