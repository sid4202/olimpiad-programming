sum_x_n = lambda start, end: ((start + end) * (end - start + 1)) // 2


def solve(n, m):
    if m <= n:
        print(m)
        return

    if ((1 + n) * n) / 2 < m:
        print(0)
        return

    left = 1
    right = n
    mid = right // 2

    while left <= right:
        mid = (left + right) // 2
        if sum_x_n(mid - 1, n) <= m:
            right = mid - 1

        elif sum_x_n(mid, n) > m:
            left = mid + 1
        else:
            break

    for i in range(n, mid - 1, -1):
        print(i)
    if sum_x_n(mid, n) != m:
        print(m - sum_x_n(mid, n))


for i in range(9,40):
    print(i)
    print('-----------------')
    solve(10, i)
    print('-----------------')
