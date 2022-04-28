def get_distance(start, finish):
    queue = [start]
    distances[start] = 0

    while queue:
        current_node = queue.pop(0)
        for node in graph[current_node]:
            if distances[node] is None:
                queue.append(node)
                distances[node] = distances[current_node] + 1

    return distances[finish]


def all_nodes_not_connected(root, nodes: list):
    checker = []

    for node in nodes:
        if node not in graph[root]:
            checker.append(-1)
        else:
            checker.append(node)

    for num in checker:
        if num != -1:
            return False

    return True


n = int(input())
m = int(input())
graph = [[]]

for i in range(n):
    graph.append([])

distances = [None for i in range(len(graph))]

for i in range(m):
    v1 = int(input())
    v2 = int(input())
    graph[v1].append(v2)

k = int(input())
nums = list(map(int, input().split(" ")))

if all_nodes_not_connected(k, nums):
    print(-1)
else:
    distances_from_k_to_node = []

    for num in nums:
        if get_distance(k, num) is not None:
            distances_from_k_to_node.append(get_distance(k, num))
        else:
            continue

    print(distances_from_k_to_node)
    print(min(distances_from_k_to_node))
