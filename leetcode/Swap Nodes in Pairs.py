# https://leetcode.com/problems/swap-nodes-in-pairs/
import time
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        first, second = head, head.next
        res = second

        while True:
            if second.next and second.next.next:
                temp = second.next
                first.next = second.next.next
                second.next = first

                first = temp
                second = first.next
            else:
                first.next = second.next
                second.next = first
                break

        return res


input = [1, 2, 3, 4]
head = ListNode(val=input[0])
cur = head
for i in range(1, len(input)):
    cur.next = ListNode(val=input[i])
    cur = cur.next

s = Solution()
res = s.swapPairs(head)
while res:
    print(res.val)
    res = res.next
