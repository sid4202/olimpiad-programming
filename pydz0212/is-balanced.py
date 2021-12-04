class Solution(object):
    def isBalanced(self, root):
        right_height = 0

        def right_height(root):
            if root is None:
                return
            nonlocal right_height
            if root.left or left.right:
                right_height_height += 1
            right_height(root.right)

        left_height = 0

        def left_height(root):
            if root is None:
                return
            nonlocal left_height
            if root.left or left.right:
                left_height += 1

            left_height(root.left)

        left_height(root)
        right_height(root)
        return max(left_height, right_height) - min(left_height, right_height) <= 1
