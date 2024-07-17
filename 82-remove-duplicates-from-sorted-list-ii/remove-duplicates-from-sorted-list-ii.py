# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(None, head)

        a, b = dummy, head

        while b:
            if b.next and b.val == b.next.val:
                while b.next and b.val == b.next.val:
                    b = b.next
                b = b.next
                a.next = b
            else:
                a, b = b, b.next

        return dummy.next