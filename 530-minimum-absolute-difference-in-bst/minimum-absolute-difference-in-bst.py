# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder traversal
        prev = [None]
        minDiff = [float('inf')]

        def dfs(r):
            if not r:
                return

            dfs(r.left)
            if prev[0] is not None:
                minDiff[0] = min(minDiff[0], r.val - prev[0])
            prev[0] = r.val
            dfs(r.right)
        dfs(root)

        return minDiff[0]