# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = l1, l2
        head = ListNode()
        ptr = head
        
        carry = 0
        while l or r:
            if l and r:
                res = l.val + r.val + carry
                carry = res // 10
                new = ListNode(res % 10)
                l, r = l.next, r.next
            elif l:
                res = l.val + carry
                carry = res // 10
                new = ListNode(res % 10)
                l = l.next
            else:
                res = r.val + carry
                carry = res // 10
                new = ListNode(res % 10)
                r = r.next
            ptr.next = new
            ptr = ptr.next

        if carry:
            new = ListNode(1)
            ptr.next = new

        return head.next

