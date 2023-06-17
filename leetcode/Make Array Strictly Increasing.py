# https://leetcode.com/problems/make-array-strictly-increasing

from bisect import bisect_right
from collections import defaultdict
from functools import cache, lru_cache
from math import inf
from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dfs(i, prev):
            if i == len(arr1):
                return 0
            ans = inf
            if prev < arr1[i]:
                ans = dfs(i + 1, arr1[i])  # don't replace
            k = bisect_right(arr2, prev)
            print(i, k, prev)
            if k < len(arr2):
                #  compare answer that don't replace and answer that replace with bisect_right value
                ans = min(ans, 1 + dfs(i + 1, arr2[k]))
            return ans

        ans = dfs(0, -inf)
        return ans if ans < inf else -1


class Solution2:
    def makeArrayIncreasing(self, arr1, arr2):
        n, ans = len(arr1), sorted(list(set(arr2)))

        @lru_cache(None)
        def dfs(i, prev):
            if i >= n:
                return 0

            j = bisect_right(ans, prev)

            swap = 1 + dfs(i + 1, ans[j]) if j < len(ans) else float("inf")
            no_swap = dfs(i + 1, arr1[i]) if arr1[i] > prev else float("inf")

            return min(swap, no_swap)

        result = dfs(0, float("-inf"))

        return result if result != float("inf") else -1


class Solution3:
    def makeArrayIncreasing(self, nums: List[int], arr2: List[int]) -> int:
        # sort arr2 and get size, set original dp with 0 -> -1
        arr2.sort()
        arrL = len(arr2)
        dp = {0: -1}
        # for num in nums
        for num in nums:
            # set up a new dp with default of infinity
            new_dp = defaultdict(lambda: inf)
            # loop current dp items
            for key, value in dp.items():
                # if value < num < new_dp[key]
                if value < num < new_dp[key]:
                    # set new dp at key to num
                    new_dp[key] = num
                    # find index in arr2
                arr2_i = bisect_right(arr2, value)
                # if index in arr2 valid and arr2 at index less than new dp at key + 1
                if arr2_i < arrL and arr2[arr2_i] < new_dp[key + 1]:
                    # store for new dp at key + 1 the value of arr2 at index
                    new_dp[key + 1] = arr2[arr2_i]
            # if new dp has not had anything filed
            if not new_dp:
                # we cannot continue
                return -1
                # otherwise, update
            dp = new_dp
            # then return as needed
        return min(dp)
