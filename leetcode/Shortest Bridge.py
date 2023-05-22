# https://leetcode.com/problems/shortest-bridge/
from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        start = next((i, j) for i in range(n) for j in range(n) if grid[i][j])
        visited = {[start]}
        island = [start]
        queue = deque([start])

        while queue:
            pos = queue.popleft()
            for d in directions:
                n_pos = (pos[0] + d[0], pos[1] + d[1])
                if n_pos[0] in range(n) and n_pos[1] in range(n) \
                        and grid[n_pos[0]][n_pos[1]] == 1 and n_pos not in visited:
                    queue.append(n_pos)
                    island.append(n_pos)
                    visited.add(n_pos)

        queue = deque(island)
        res = 0
        while queue:
            temp = deque()
            for pos in queue:
                for d in directions:
                    n_pos = (pos[0] + d[0], pos[1] + d[1])
                    if n_pos[0] in range(n) and n_pos[1] in range(n) and n_pos not in visited:
                        if grid[n_pos[0]][n_pos[1]] == 1:
                            return res
                        temp.append(n_pos)
                        visited.add(n_pos)
            queue = temp
            res += 1


s = Solution()
grid = [[0,1,0],[0,0,0],[0,0,1]]
print(s.shortestBridge(grid))
