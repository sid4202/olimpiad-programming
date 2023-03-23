class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def convert(self, arr):
        if len(arr) == 0:
            return None

        if len(arr) == 1:
            return TreeNode(arr[0])

        mid = len(arr) // 2
        root = TreeNode(arr[mid])
        less_mid = arr[:mid]
        more_mid = arr[mid + 1:]

        root.left = self.convert(less_mid)
        root.right = self.convert(more_mid)



    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.convert(nums)