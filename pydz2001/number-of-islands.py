class Solution(object):
    def __init__(self):
        self.visited = set()

    def grid_to_graph(self, grid):
        previous_max_node = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    grid[x][y] = int(previous_max_node + 1)
                    previous_max_node += 1
                grid[x][y] = int(grid[x][y])
        print(grid)
        graph = [[]]
        for i in range(previous_max_node + 1):
            graph.append([])

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y]:
                    if y + 1 <= len(grid[x]) - 1:
                        if grid[x][y + 1]:
                            graph[grid[x][y]].append(grid[x][y + 1])

                    if x + 1 <= len(grid) - 1:
                        if grid[x + 1][y]:
                            graph[grid[x][y]].append(grid[x + 1][y])

                    if y - 1 >= 0:
                        if grid[x][y - 1]:
                            graph[grid[x][y]].append(grid[x][y - 1])

                    if x - 1 >= 0:
                        if grid[x - 1][y]:
                            graph[grid[x][y]].append(grid[x - 1][y])

        return graph

    def dfs(self, start):
        self.visited.add(start)

        for node in graph[start]:
            if node in self.visited:
                continue

            self.dfs(node)

    def numIslands(self, grid):
        global graph
        graph = self.grid_to_graph(grid)
        islands_count = 0
        print(graph)
        for i in range(len(graph)):

            if i in self.visited:
                continue

            self.dfs(i)
            islands_count += 1
        return islands_count - 2
