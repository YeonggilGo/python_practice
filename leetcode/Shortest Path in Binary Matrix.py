from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        res = 1
        queue = [(0, 0)]
        directions = [(1, 0), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1), (-1, 0), (0, -1)]
        while queue:
            temp_queue = []
            for y, x in queue:
                if (y, x) == (n - 1, n - 1):
                    return res
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and grid[ny][nx] == 0:
                        grid[ny][nx] = 1
                        temp_queue.append((ny, nx))
            queue = temp_queue
            res += 1
        return -1


grid = [[0, 1], [1, 0]]
s = Solution()
print(s.shortestPathBinaryMatrix(grid))
