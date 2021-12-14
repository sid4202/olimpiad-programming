class Solution(object):
    def get_max_depth(self, root):
        if root is None:
            return 0

        left_depth = self.get_max_depth(root.left)
        right_depth = self.get_max_depth(root.right)

        return max(left_depth, right_depth) + 1


    def isBalanced(self, root):
        if root is None:
            return True

        right_branch = self.get_max_depth(root.right)
        left_branch = self.get_max_depth(root.left)
        if max(right_branch, left_branch) - min(right_branch,left_branch)>1:
            return False
        return self.isBalanced(root.right) and self.isBalanced(root.left)