# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = slow.next
        while slow and fast:
            if slow == fast:
                return True
            # 1 step
            slow = slow.next
            # 2 step
            if not fast.next:
                return False
            fast = fast.next.next
        return False
