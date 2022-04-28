class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def set_biggest_number(root : TreeNode, max_value):
    if root is None:
        return max_value
    if root.value > max_value:
        max = root.value
    return max(set_biggest_number(root.right, max_value), set_biggest_number(root.left, max_value))


"""def get_biggest_number(root, max=-1000000):
    if root is None:
        return
    if root.value > max:
        max = root.value
    return max([get_biggest_number(root.right, max), get_biggest_number(root.left, max)])
"""

def print_tree(root):
    if root.left is None or root.right is None:
        return
    print(root.value)
    print(root.left.value, root.right.value)
    print_tree(root.left)
    print_tree(root.right)


root = TreeNode(50)
root.left = TreeNode(25)
root.right = TreeNode(75)
root.left.left = TreeNode(1)
root.left.right = TreeNode(30)
root.right.left = TreeNode(70)
root.right.right = TreeNode(90)
root.right.left.left = TreeNode(60)
root.right.left.right = TreeNode(73)
root.right.right.right = TreeNode(100)
print(set_biggest_number(root,root.value))
