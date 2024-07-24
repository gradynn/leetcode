# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def findMaxDepth(subRoot: Optional[TreeNode], depth: int) -> int:
            if not subRoot:
                return depth
            return max(
                findMaxDepth(subRoot.left, depth + 1),
                findMaxDepth(subRoot.right, depth + 1)
            )

        return findMaxDepth(root, 0)
