def dfs(start):
    visited.add(start)

    for node in graph[start]:
        if node in visited:
            continue

        dfs(node)


def is_way(a: int, b: int):
    dfs(a)
    if b in visited:
        return True
    return False


n = int(input())
k = int(input())
graph = [[]]
visited = set()

for i in range(n):
    graph.append([])

for i in range(k):
    v1 = int(input())
    v2 = int(input())
    graph[v1].append(v2)
print(graph)
p1 = int(input())
p2 = int(input())
print(is_way(p1,p2))