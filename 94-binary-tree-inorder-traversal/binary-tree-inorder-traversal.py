# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        iot = []

        s = []
        current = root
        while True:
            if current:
                s.append(current)
                current = current.left
            elif s:
                current = s.pop()
                iot.append(current.val)
                current = current.right
            else:
                break

        return iot
            