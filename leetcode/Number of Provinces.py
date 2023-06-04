from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        res = 0
        n = len(isConnected)
        visited = [0 for a in range(n)]

        for i in range(n):
            if visited[i]:
                continue
            res += 1
            visited[i] = 1
            queue = [j for j in range(n) if isConnected[i][j] and j != i]
            while queue:
                j = queue.pop()
                if visited[j]:
                    continue
                visited[j] = 1
                queue.extend([k for k in range(n) if isConnected[j][k]])
        return res


input = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
s = Solution()
print(s.findCircleNum(input))
