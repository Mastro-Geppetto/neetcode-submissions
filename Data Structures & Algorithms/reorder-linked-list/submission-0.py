# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        nxt = prv = None
        while ptr:
            print(ptr.val)
            nxt = ptr.next
            ptr.next = prv
            prv = ptr
            ptr = nxt
        return prv

    def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slow = head
        fast = head.next
        while slow and fast:
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next.next
        return slow
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0. if size < 3, do nothing
        if not head or not head.next: # empty or 1 element
            return
        if head.next and not head.next.next: # < 3
            return
        # 1. find mid
        mid = self.get_mid( head )
        if not mid:
            return
        print('mid', mid.val)
        # 2. break
        nxt = mid.next
        # 3. set mid.next = None
        mid.next = None
        # 4. reverser 2nd half
        reversed_l = self.rev(nxt)
        print('rev 1st', reversed_l.val)
        # 5. merge
        hNxt = head.next
        rNxt = reversed_l.next
        while reversed_l:
            hNxt = head.next
            head.next = reversed_l
            rNxt = reversed_l.next
            reversed_l.next = hNxt
            head = hNxt
            reversed_l = rNxt
