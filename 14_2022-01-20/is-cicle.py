def is_cicle(start):
    print("start:", start)
    visited.add(start)

    for node in graph[start]:
        print(visited)
        print(node)
        print(node in visited)
        if node in visited:
            return True

        return is_cicle(node)


graph = [[],
         [2,3],
         [1,3],
         [1,4],
         [3,5],
         [4],
         ]
visited = set()
"""
for i in range(n):
    graph.append([])

for i in range(k):
    v1 = int(input())
    v2 = int(input())
    graph[v1].append(v2)
print(graph)
p1 = int(input())
p2 = int(input())
"""

print(is_cicle(2))
