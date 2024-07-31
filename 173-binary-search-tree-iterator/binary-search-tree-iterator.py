# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self, root: Optional[TreeNode]):
        startNode = self.ListNode(float('-inf'))

        ptr = [startNode]
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)

            newNode = self.ListNode(node.val)
            ptr[0].next = newNode
            ptr[0] = ptr[0].next

            dfs(node.right)
        dfs(root)
        self.itr = startNode

    def next(self) -> int:
        self.itr = self.itr.next
        return self.itr.val

    def hasNext(self) -> bool:
        return self.itr.next is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()