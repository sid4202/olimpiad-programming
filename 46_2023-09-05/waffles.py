def solve():
    pass


t = int(input())
for _ in range(t):
    n, m, d = list(map(int, input().split()))
    shop_cords = list(map(int, input().split()))
    shop_cords.append(1)
    shop_cords.append(n + 1)

    shop_cords.sort()

    waffles_eaten = 0
    shops_to_delete = 0

    for i in range(1, m + 1):
        y2 = 1 + ((shop_cords[i + 1] - shop_cords[i - 1] - 1) // d)
        y1 = (shop_cords[i] - shop_cords[i - 1] - 1) // d + (shop_cords[i + 1] - shop_cords[i] - 1) // d + 2

        if y2 < y1:
            shops_to_delete += 1

        if i == 1:
            waffles_eaten += 2 + ((shop_cords[i] - shop_cords[i - 1] - 1) // d)
        else:
            waffles_eaten += 1 + ((shop_cords[i] - shop_cords[i - 1] - 1) // d)
    waffles_eaten += ((shop_cords[-1] - shop_cords[-2] - 1) // d)

    if shops_to_delete:
        print(waffles_eaten - 1, shops_to_delete)
    else:
        print(waffles_eaten, m)