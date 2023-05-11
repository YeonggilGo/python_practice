# https://leetcode.com/problems/add-two-numbers/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = [], []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        print(num1, num2)
        num1 = int(''.join(num1[::-1]))
        num2 = int(''.join(num2[::-1]))
        res_li = list(str(num1 + num2))[::-1]
        res = ListNode()
        temp = res
        for i, n in enumerate(res_li):
            temp.val = n
            if i != len(res_li) - 1:
                temp.next = ListNode()
                temp = temp.next

        return res
