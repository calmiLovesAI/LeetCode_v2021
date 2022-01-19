# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        if p1 is None and p2 is None:
            return None
        p = ListNode()
        res = p
        while p1 and p2:
            if p1.val < p2.val:
                p.val = p1.val
                p1 = p1.next
            else:
                p.val = p2.val
                p2 = p2.next
            p.next = ListNode()
            p = p.next

        while p1:
            p.val = p1.val
            p1 = p1.next
            if p1:
                p.next = ListNode()
                p = p.next

        while p2:
            p.val = p2.val
            p2 = p2.next
            if p2:
                p.next = ListNode()
                p = p.next
        return res


# 写的简单一点
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(-1)
        pre = pre_head
        while list1 and list2:
            if list1.val < list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        pre.next = list1 if list1 else list2
        return pre_head.next
