# https://leetcode.com/problems/uncrossed-lines/
from typing import List, Tuple


class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        if n > m:
            return self.maxUncrossedLines(nums2, nums1)

        dp = [0] * (n + 1)
        for i in range(m):
            for j in range(n)[::-1]:
                if nums1[i] == nums2[j]:
                    dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j+1], dp[j])
        return dp[n]


s = Solution()
# nums1 = [3, 1, 2, 1, 4, 1, 2, 2, 5, 3, 2, 1, 1, 4, 5, 2, 3, 2, 5, 5]
# nums2 = [2, 4, 1, 2, 3, 4, 2, 4, 5, 5, 1, 1, 2, 1, 1, 1, 5, 4, 1, 4, 2, 1, 5, 4, 2, 3, 1, 5, 2, 1]

nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
print(s.maxUncrossedLines(nums1, nums2))
