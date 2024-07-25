# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root or (not root.left and not root.right):
            return True
        
        q = [root.left, root.right]
        while q:
            l = len(q)
            for i in range(l // 2):
                if not q[i] and q[l - i - 1]:
                    return False
                elif q[i] and not q[l - i - 1]:
                    return False
                elif not q[i] and not q[l - i - 1]:
                    pass
                elif q[i].val != q[l - i - 1].val:
                    return False
            for i in range(l):
                node = q.pop(0)
                if node:
                    q.append(node.left)
                    q.append(node.right)

        return True