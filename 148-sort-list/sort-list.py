# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # find middle
        s = f = head
        while f and f.next and f.next.next:
            s = s.next
            f = f.next.next
        temp = s
        s = s.next
        temp.next = None

        sorted_left = self.sortList(head)
        sorted_right = self.sortList(s)
        
        dummy = ListNode()
        ptr = dummy
        while sorted_left or sorted_right:
            if not sorted_left:
                ptr.next = sorted_right
                break
            elif not sorted_right:
                ptr.next = sorted_left
                break

            if sorted_right.val >= sorted_left.val:
                ptr.next = sorted_left
                sorted_left = sorted_left.next
            else:
                ptr.next = sorted_right
                sorted_right = sorted_right.next
            ptr = ptr.next
            
        return dummy.next
