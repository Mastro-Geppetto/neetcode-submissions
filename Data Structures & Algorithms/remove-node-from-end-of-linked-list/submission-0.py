# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def count(self, head: Optional[ListNode]) -> int:
        n=0
        while head:
            n += 1
            head = head.next
        return n

    def rmNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        nxt = head.next
        head.next = self.rmNthFromEnd(nxt, n-1)
        if not n:
            return nxt
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        sz = self.count(head)
        rmPos = sz-n+1
        if rmPos == 1:
            return head.next
        # for other
        prev = None
        curr = head
        nxt = head.next
        while rmPos > 1:
            prev = curr
            curr = nxt
            nxt = curr.next
            rmPos -= 1
        if not prev:
            print('1st pos del')
            curr.next = None
            head = nxt
        else:
            prev.next = nxt
        return head

