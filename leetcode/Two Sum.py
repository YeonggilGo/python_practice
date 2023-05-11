# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        raise Exception("Can't find answer")


nums = [2, 7, 11, 15]
target = 9

s = Solution()
print(s.twoSum(nums, target))
