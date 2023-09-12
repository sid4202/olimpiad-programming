def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


n, k = list(map(int, input().split()))
print(lcm(n, k))
