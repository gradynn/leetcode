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
            if a.val == b.val:
                while b and a.val == b.val:
                    b = b.next
                a.next = b

            if not b:
                break
            
            a, b = b, b.next

        return dummy.next