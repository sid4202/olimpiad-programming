class Solution(object):
    def postorder_traversal(self, root, arr):
        if root is None:
            return
        self.postorder_traversal(root.left, arr)
        self.postorder_traversal(root.right, arr)
        arr.append(root.val)

    def postorderTraversal(self, root):
        arr = []
        if root is None:
            return []
        self.postorder_traversal(root, arr)
        return arr
