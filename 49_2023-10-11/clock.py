def gcd(a, b):
    if a % b == 0:
        return b

    return gcd(b, a % b)


def reduce_fraction(number, divisor):
    gcd_of_fraction = gcd(divisor, number)
    if gcd_of_fraction != 1:
        number //= gcd_of_fraction
        divisor //= gcd_of_fraction

    return int(number), int(divisor)


t = int(input())

for _ in range(t):
    n, a, b, c = list(map(int, input().split()))
    if a / n <= b / c:
        h = a + 1
    else:
        h = a

    minutes_number = h
    minutes_divisor = n - 1

    minutes_number, minutes_divisor = reduce_fraction(minutes_number, minutes_divisor)

    if minutes_number / minutes_divisor == 1:
        h += 1
        minutes_number = 0

    if h == n:
        h = 0

    print(h, minutes_number, minutes_divisor)







