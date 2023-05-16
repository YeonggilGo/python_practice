# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        li = [ListNode()]
        while head:
            li.append(head)
            head = head.next

        li.append(None)

        if len(li) <= 3:
            return li[1]

        p1, p2 = k, -k - 1
        li[p1], li[p2] = li[p2], li[p1]
        li[p1].next, li[p2].next = li[p1 + 1], li[p2 + 1]
        li[p1 - 1].next, li[p2 - 1].next = li[p1], li[p2]

        return li[1]


input = [1, 2]
k = 1

head = ListNode(val=input[0])
cur = head
for i in range(1, len(input)):
    cur.next = ListNode(val=input[i])
    cur = cur.next
s = Solution()
node = s.swapNodes(head, k)
while node:
    print(node.val)
    node = node.next
