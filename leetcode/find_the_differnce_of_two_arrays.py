# https://leetcode.com/problems/find-the-difference-of-two-arrays/
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        inter = set(nums1).intersection(set(nums2))
        nums1 = list(set(nums1) - inter)
        nums2 = list(set(nums2) - inter)
        return [nums1, nums2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
print(Solution().findDifference(nums1, nums2))
