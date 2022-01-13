# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢指针找到倒数第n个结点就行
        slow = head
        pre = ListNode(next=slow)
        fast = head

        for _ in range(n-1):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            pre = pre.next
            fast = fast.next

        # 移除slow指向的那个结点
        pre.next = slow.next
        slow.next = None
        return pre.next if slow == head else head

