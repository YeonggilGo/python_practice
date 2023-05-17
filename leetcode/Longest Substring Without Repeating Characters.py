# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        basket = {}
        for right_index, value in enumerate(s):
            if value not in basket:
                basket[value] = right_index
            elif value in basket and basket[value] < left:
                basket[value] = right_index
            else:
                left = basket[value] + 1
                basket[value] = right_index
            max_len = max(max_len, right_index - left + 1)
        return max_len


input = 'abcabcbb'
s = Solution()
print(s.lengthOfLongestSubstring(input))
