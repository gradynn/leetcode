"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ptr = head
        
        newHead = Node(0)
        newPtr = newHead

        mapRandom = {}

        while ptr:
            newNode = Node(ptr.val)
            newPtr.next = newNode
            newPtr = newPtr.next
            mapRandom[ptr] = newNode
            ptr = ptr.next
        
        newHead = newHead.next
        ptr = head
        newPtr = newHead

        while ptr:
            if ptr.random:
                newPtr.random = mapRandom[ptr.random]
            ptr, newPtr = ptr.next, newPtr.next

        return newHead