# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        t, h = head, head.next

        while t != h:
            if not h or not h.next:
                return False
            t = t.next
            h = h.next.next
        
        return True