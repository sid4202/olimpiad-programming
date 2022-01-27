class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        queue = [root]
        max_distance = 1

        while queue:
            current = queue.pop(0)

            if current is not None:
                if current.left or current.right is not None:
                    max_distance += 1
                for node in [current.right, current.left]:
                    if node is not None:
                        queue.append(node)
            else:
                continue
        return max_distance
