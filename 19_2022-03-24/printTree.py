class Queue:
    def __init__(self, elements):
        self.arr = elements

    def add(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)


class Solution:
    res = []

    def get_depth(self, node):
        if not node:
            return 0
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1

    def fill_res(self, root):
        for i in range(self.get_depth(root)):
            self.res.append([])
            for j in range(2 ** self.get_depth(root) - 1):
                self.res[i].append("")

    def bfs(self, root):
        queue = Queue([root])
        level = 0
        length = len(self.res[0])
        print(length)
        self.res[level][(len(self.res[0]) - 1) // 2] = str(root.val)
        root.index = length - 1 // 2
        while queue.size():
            size = queue.size()
            level += 1

            for i in range(size):
                node = queue.pop()
                swift = 2 ** (self.get_depth(root) - 1 - (level - 1) - 1)
                l_c_pos = node.index
                r_c_pos = node.index
                if node.left:
                    queue.add(node.left)
                    print("l_pos", self.res[level - 1].index(str(node.val)))
                    index = l_c_pos - swift
                    self.res[level][index] = str(node.left.val)
                    node.left.index = index

                if node.right:
                    queue.add(node.right)
                    print("pos", self.res[level - 1][::-1].index(str(node.val)))
                    print(("index", length - self.res[level - 1][::-1].index(str(node.val))))
                    index = r_c_pos + swift
                    print("index", index)
                    self.res[level][index] = str(node.right.val)
                    node.right.index = index

    def printTree(self, root):
        self.res = []
        self.fill_res(root)
        self.bfs(root)
        return self.res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(sol.printTree(root))