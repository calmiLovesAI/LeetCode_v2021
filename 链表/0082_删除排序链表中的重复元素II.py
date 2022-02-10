# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "val: {}".format(self.val)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre = ListNode(-1)
        ans = pre
        p = head
        pre.next = p
        q = head.next
        while q:
            if p.val != q.val:
                pre = pre.next
                p = p.next
                q = q.next
            else:
                while q and q.val == p.val:
                    q = q.next
                pre.next = q
                if q is None:
                    return ans.next
                p = q
                q = p.next
        return ans.next


if __name__ == '__main__':
    head = ListNode(1)
    p1 = ListNode(1)
    p2 = ListNode(1)

    head.next = p1
    p1.next = p2


    def print_linkedlist(head: ListNode):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    print_linkedlist(Solution().deleteDuplicates(head))
