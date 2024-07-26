# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None
        
        root = TreeNode(val=postorder[len(postorder) - 1])

        index = inorder.index(root.val)
        leftInorder, rightInorder = inorder[:index], inorder[index + 1:]
        leftPostorder, rightPostorder = postorder[:len(leftInorder)], postorder[len(leftInorder):-1]

        root.left = self.buildTree(leftInorder, leftPostorder)
        root.right = self.buildTree(rightInorder, rightPostorder)

        return root