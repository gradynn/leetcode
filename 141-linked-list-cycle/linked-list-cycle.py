# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        count = 1

        while ptr:
            if count > 10000:
                return True
            ptr = ptr.next
            count += 1
    
        return False
