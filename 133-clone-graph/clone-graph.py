"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        q = deque([node])
        visited.add(node)

        mapping = {}

        while q:
            cur = q.popleft()

            newNode = Node(cur.val)
            mapping[cur] = newNode

            for n in cur.neighbors:
                if n not in visited:
                    q.append(n)
                    visited.add(n)

        visited = set()
        q.append(node)
        visited.add(node)
        while q:
            cur = q.popleft()
            for n in cur.neighbors:
                mapping[cur].neighbors.append(mapping[n])
                if n not in visited:
                    q.append(n)
                    visited.add(n)

        return mapping[node]