# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        s = [(root, targetSum)]
        while s:
            node, remainingSum = s.pop()

            if not node.left and not node.right and remainingSum - node.val == 0:
                return True

            if node.right:
                s.append((node.right, remainingSum - node.val))
            if node.left:
                s.append((node.left, remainingSum - node.val))

        return False