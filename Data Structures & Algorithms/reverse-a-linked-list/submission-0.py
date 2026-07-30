# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        next_list = []
        while head:
            #print(head.val)
            next_list.append(head)
            head = head.next
        # reverse linkage
        prev_ptr = None
        for curr_ptr in next_list:
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
        return next_list[-1]