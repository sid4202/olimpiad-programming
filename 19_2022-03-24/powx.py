class TreeNode:
    def __init__(self, value):
        self.val = val
        self.left = None
        self.right = None


class Queue:
    def __init__(self, elements):
        self.arr = elements

    def add(self, value):
        self.arr.append(value)

    def pop(self):
        return self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def print(self):
        for node in self.arr:
            print(node.value, end=' ')
        print()


class Solution:
    res = []

    def get_depth(self, node):
        if not node:
            return 0
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1

    def fill_res(self, root):
        for i in range(self.get_depth(root)):
            self.res.append([])
            for i in range(2**self.get_depth(root) - 1):
                self.res[i].append("")


    def bfs(self,root):
        queue = Queue([root])
        level = 0
        self.res[level][len(self.res - 1)/2] = str(root.val)
        while queue.size():
            size = queue.size()
            level+=1
            for i in range(size):
                node = queue.pop()

                if node.left:
                    queue.add(node.left)
                    self.res[level][self.res[level-1].index(node.value) - 1] = str(node.left.val)

                if node.right:
                    queue.add(node.right)
                    self.res[level][self.res[level - 1].index(node.value) + 1] = str(node.right.val)

    def printTree(self, root):
        self.fill_res(root)
        self.bfs(root)
        return self.res
