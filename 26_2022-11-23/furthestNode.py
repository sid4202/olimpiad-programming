class FurthestNodeFinder:
    def __init__(self):
        self.visited = set()
        self.A = 0
        self.N = 0
        self.graph = []

    def furthestNode(self, node, depth):
        print(self.A, self.N)
        if node in self.visited:
            return
        self.visited.add(node)

        if depth > self.A:
            self.A = depth
            self.N = node

        node = self.graph[node]

        for child in node:
            self.furthestNode(child, depth + 1)

    def process(self, node):
        self.furthestNode(node, 0)
        return self.N


graph = [
    [1],
    [0, 4],
    [3],
    [2, 4],
    [1, 3, 5],
    [4]
]

sol = FurthestNodeFinder()

sol.graph = graph

print(sol.process(5))
