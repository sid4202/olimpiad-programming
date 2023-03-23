class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.visited = []

    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

root = TreeNode()
root.left = TreeNode()
root.right = TreeNode()
root.left.left = TreeNode()
answer = Solution().maxDepth(root)
print(answer)
assert(answer == 3)