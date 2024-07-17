# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        newHead = ListNode(next=head)

        a, b = newHead, newHead.next
        
        c = b
        for i in range(n - 1):
            c = c.next

        while c.next:
            a = b
            b = b.next
            c = c.next

        a.next = b.next

        return newHead.next