a, b, c = list(map(int, input().split()))
n = int(input())

products = list(map(int, input().split()))

if a > c:
    best_price = a
    print(best_price)
    exit()
else:
    best_price = a + b

best_price_x = 0
best_price_y = c - a + 1

bag = [[0 for j in range(c - a + 2)] for i in range(n + 1)]
bag_map = [[False for j in range(c - a + 2)] for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, c - a + 2):
        current_product = products[i - 1]

        if j - current_product < 0:
            price_with_current_product = current_product
        else:
            price_with_current_product = bag[i - 1][j - current_product] + current_product

        if bag[i - 1][j] < j and price_with_current_product < j:
            continue

        bag[i][j] = min(bag[i - 1][j], price_with_current_product)

        if bag[i][j] == bag[i - 1][j] and bag[i - 1][j] == 0:
            if price_with_current_product >= j:
                bag[i][j] = price_with_current_product

        if bag[i][j] == price_with_current_product:
            bag_map[i][j] = True

for i in range(n + 1):
    if 0 < bag[i][c - a + 1] < best_price:
        best_price = a + bag[i][c - a + 1]
        best_price_x = i

answer = []
i = best_price_x
j = best_price_y

while i > 0:
    if bag_map[i][j]:
        answer.append(i)
        j -= products[i - 1]
        i -= 1
    else:
        i -= 1

answer.sort()

if best_price <= a + b:
    print(best_price)
    print(len(answer), *answer)
else:
    print(-1)
