# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        s = [(root, "")]
        while s:
            node, rSum = s.pop()
            if not node.left and not node.right:
                total += int(rSum + str(node.val))

            if node.left:
                s.append([node.left, rSum + str(node.val)])
            if node.right:
                s.append([node.right, rSum + str(node.val)])
        
        return total
