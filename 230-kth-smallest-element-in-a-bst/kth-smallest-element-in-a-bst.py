# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        iot = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            
            iot.append(node.val)

            dfs(node.right)
        dfs(root)

        return iot[k - 1]