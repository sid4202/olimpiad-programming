class Solution(object):
    def invertTree(self, root):
        if root is None:
            return
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
