class Solution(object):
    def isUnivalTree(self, root):
        data = root.val

        def checker(root, data):
            if not root:
                return True
            if root.val != data:
                return False
            return checker(root.right, data) and checker(root.left, data)

        return checker(root, data)
