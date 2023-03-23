graph = [
    [],
    [2, 7],
    [5, 4, 3, 1],
    [2, 4],
    [2, 3, 5],
    [2, 4, 6],
    [5],
    [1]
]


def furthest_node(start_node, graph):
    queue = [start_node]
    visited = set([start_node])

    while queue:
        print(queue)
        current_node = queue.pop(0)

        for child in graph[current_node]:
            if child not in visited:
                queue.append(child)
                visited.add(child)

    return current_node


print(furthest_node(1, graph))
