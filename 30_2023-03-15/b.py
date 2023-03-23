k = int(input())

for t in range(k):
    d = list(map(int, input().split()))[2]
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))

    map_p = dict()

    for i in range(len(p)):
        map_p[p[i]] = i

    answer = 10000000
    for i in range(len(a) - 1):
        distance = map_p[a[i + 1]] - map_p[a[i]]
        if d < len(p) - 1:
            distance_to_spread = d + 1 - distance
            result = min(distance_to_spread, distance)
        else:
            result = distance

        answer = min(result, answer)

    answer = max(answer, 0)
    print(answer)
