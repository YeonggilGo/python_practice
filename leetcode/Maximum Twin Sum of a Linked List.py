# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        basket = []
        while head:
            basket.append(head.val)
            head = head.next
        twin_sum = [basket[i] + basket[-i - 1] for i in range(len(basket) // 2)]
        return max(twin_sum)


input = [4, 2, 2, 3]
head = ListNode(input[0])
cur = head
for i in range(1, len(input)):
    head.next = ListNode(input[i])
    head = head.next

s = Solution()
print(s.pairSum(cur))
