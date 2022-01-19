# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 迭代
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = head, head.next

        while cur is not None:
            t = cur.next
            cur.next = pre
            if pre == head:
                pre.next = None
            pre = cur
            cur = t

        return pre


# 递归
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        # 将head之后的所有结点看作一个整体
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head



# 打印链表
def print_linkedlist(head: ListNode):
    while head:
        print("{} ->".format(head.val), end="")
        head = head.next
    print()


if __name__ == '__main__':
    head = ListNode(1)
    p = ListNode(2)
    head.next = p
    m = ListNode(3)
    n = ListNode(4)
    p.next = m
    m.next = n

    print_linkedlist(Solution().reverseList(head))
