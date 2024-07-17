# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        newHead = ListNode(next=head)

        a, b = newHead, head

        for i in range(left - 1):
            a, b = a.next, b.next

        c = b.next
        for i in range(right - left):
            temp = c.next
            c.next = b
            b = c
            c = temp

        a.next.next = c
        a.next = b

        return newHead.next
        