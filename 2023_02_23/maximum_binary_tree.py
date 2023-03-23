class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        root = TreeNode(max(nums))

        root_index = nums.index(max(nums))

        right_branch = nums[root_index + 1:]

        left_branch = nums[:root_index]

        root.left = self.constructMaximumBinaryTree(left_branch)
        root.right = self.constructMaximumBinaryTree(right_branch)

        return root



