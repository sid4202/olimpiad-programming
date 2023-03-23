class Solution:
    def __init__(self):
        self.visited = set()

    def bfs(self,start_node, isConnected):
        queue = [start_node]

        while queue:
            current_node = queue.pop(0)
            if current_node not in self.visited:
                for child in isConnected[current_node]:
                    if child == 1:
                        queue.append(isConnected[current_node].index(child))

            self.visited.add(current_node)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        answer = 0
        for node in range(len(isConnected)):
            if node not in self.visited:
                self.bfs(node, isConnected)
                answer += 1

        return answer
