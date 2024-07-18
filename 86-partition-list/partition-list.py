# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(0, None)
        dummy2 = ListNode(0, None)

        itr, build1, build2 = head, dummy1, dummy2  
        
        while itr:
            if itr.val < x:
                build1.next = itr
                build1 = build1.next
            else:
                build2.next = itr
                build2 = build2.next      
            itr = itr.next
        
        build1.next = dummy2.next
        build2.next = None

        return dummy1.next
