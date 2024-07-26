# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return root

        s = [root]
        dummy = TreeNode()
        ptr = dummy
        while s:
            node = s.pop()

            # process node
            ptr.left, ptr.right = None, node

            # append children
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)

            # move ptr
            ptr = ptr.right

        return root