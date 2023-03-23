class Solution:
    def edges_to_graph(self, edges):
        graph = []
        number_of_nodes = 0
        maximum = edges[0][0]
        for i in range(len(edges)):
            for j in range(len(edges[i])):
                if edges[i][j] > maimum:
                    maximum = edges[i][j]
        graph = [graph.append([]) for i in range(maximum + 1)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        return graph

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        queue = [source]
        graph = self.edges_to_graph(edges)

        while queue:
            if destination in queue:
                return True

            current_node = queue.pop(0)

            for node in graph[current_node]:
                queue.append(node)

        return False
