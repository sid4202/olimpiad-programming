def solve(arr):
    if 1 in arr:
        return True

    if min(arr) > len(arr):
        return False

    for i in range(len(arr)):
        if i + 1 >= arr[i]:
            return True

    return False


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    print("YES") if solve(arr) else print("NO")
    