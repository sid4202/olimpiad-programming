class Solution(object):
    def isBalanced(self, root):
        def height_tree(root,left,height = 0):
            
            if root is None:
                return height
            if left:
                return height_tree(root.left, True, height)

        right_height = height_tree(root.right,False)
        left_height = height_tree(root.left,True)
        print(right_height, left_height)
        return max(left_height, right_height) - min(left_height, right_height) <= 1
