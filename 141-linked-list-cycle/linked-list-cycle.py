# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head
        seen = set()

        while ptr:
            if ptr in seen:
                return True
            seen.add(ptr)
            ptr = ptr.next

        return False
