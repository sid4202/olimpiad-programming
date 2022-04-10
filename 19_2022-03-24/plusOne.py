def inc(n:int):
    a = 1

    while n & a != 0:
        a = a << 1
    a |= ~a
    return -(n ^ a)


n = int(input())
print(inc(n))