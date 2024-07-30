# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        iot = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            iot.append(node.val)
            dfs(node.right)  
        dfs(root)

        if iot != sorted(list(set(iot))):
            return False
        else:
            return True