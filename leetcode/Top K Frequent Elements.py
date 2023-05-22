# https://leetcode.com/problems/top-k-frequent-elements/
# collections.Counter를 쓰면 더 쉽게도 가능하다.
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        memory_dict = dict()

        for num in nums:
            memory_dict.update({num: memory_dict.get(num, 0) + 1})

        return sorted([key for key in memory_dict], key=lambda x:-memory_dict[x])[:k]


nums = [5,3,1,1,1,3,73,1]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
