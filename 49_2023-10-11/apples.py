def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


power_of_2 = set(list([2 ** i for i in range(0, 32)]))


def solve():
    apple_count, people = list(map(int, input().split()))

    if apple_count == 1 and people not in power_of_2:
        return -1

    if apple_count % people == 0:
        return 0

    if people / gcd(apple_count, people) not in power_of_2:
        return -1

    answer = 0

    if apple_count < people:
        answer += apple_count
        apple_count *= 2

    elif apple_count > people:
        apple_count %= people

    while apple_count != people:
        if apple_count < people:
            answer += apple_count
            apple_count *= 2
            continue

        elif apple_count > people:
            apple_count %= people

    return answer


t = int(input())
for _ in range(t):
    print(solve())
