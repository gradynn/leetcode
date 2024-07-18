# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        ptr, length = head, 1
        while ptr.next:
            ptr = ptr.next
            length += 1

        spacing = k % length
        
        l, r = head, head
        for i in range(spacing):
            r = r.next
        
        while r.next:
            l, r = l.next, r.next
        
        r.next = head
        head = l.next
        l.next = None
        
        return head
