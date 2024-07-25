# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root = TreeNode(preorder[0])
        
        i = 0
        while i < len(inorder):
            if inorder[i] == root.val:
                break
            i += 1

        leftInorder = inorder[:i]
        leftPreorder = preorder[1:1 + i]

        rightInorder = inorder[i + 1:]
        rightPreorder = preorder[1 + i:]

        root.left = self.buildTree(leftPreorder, leftInorder)
        root.right = self.buildTree(rightPreorder, rightInorder)

        return root
