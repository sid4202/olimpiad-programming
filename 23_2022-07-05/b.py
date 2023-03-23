t = int(input())

for i in range(t):
    s2 = input()

    if len(s2) == 1:
        print("NO")
        continue

    if s2[0] == "B":
        print("NO")
        continue

    if s2[::-1][0] == "A":
        print("NO")
        continue

    b_arr = []

    for c in s2[::-1]:
        if c == "B":
            b_arr.append(c)
        if c == "A":
            if len(b_arr) > 0:
                b_arr.pop(0)

    if len(b_arr) == 0:
        print("YES")
    else:
        print("NO")