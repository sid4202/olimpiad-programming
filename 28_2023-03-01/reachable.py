class Solution:
    def edges_to_graph(self, edges, n):
        graph = []
        for i in range(n):
            graph.append([])

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        answer = 0
        visited = set()
        restricted_list = set(restricted)

        graph = self.edges_to_graph(edges, n)
        queue = [0]
        while queue:
            node_num = queue.pop(0)
            current_node = graph[queue.pop(0)]
            for child in current_node:
                if child not in visited and child not in restricted_list:
                    queue.append(child)
                    answer += 1
            visited.add(node_num)

        return answer
