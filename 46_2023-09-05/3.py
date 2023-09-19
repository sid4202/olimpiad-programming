def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


x1, y1, x2, y2 = list(map(int, input().split()))

sx = abs(x2 - x1)

sy = abs(y2 - y1)

print(gcd(max(sx, sy), min(sx, sy)) + 1)
