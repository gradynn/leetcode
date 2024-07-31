# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.s = []

        while root:
            self.s.append(root)
            root = root.left

    def next(self) -> int:
        res = self.s.pop()
        cur = res.right
        while cur:
            self.s.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:
        return self.s
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()