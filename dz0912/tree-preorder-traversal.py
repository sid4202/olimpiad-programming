class Solution(object):
    def preorder_traversal(self, root, arr):
        if root is None:
            return
        arr.append(root.val)
        self.preorder_traversal(root.left, arr)
        self.preorder_traversal(root.right, arr)

    def preorderTraversal(self, root):
        if root is None:
            return []
        arr = []
        self.preorder_traversal(root, arr)
        return arr

