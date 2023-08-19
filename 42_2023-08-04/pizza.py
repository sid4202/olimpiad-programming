a, b, c = list(map(int, input().split()))
n = int(input())

products = list(map(int, input().split()))

if a > c:
    best_price = a
else:
    best_price = a + b

best_price_x = 0
best_price_y = 0

bag = [[best_price for j in range(n + 1)] for i in range(n + 1)]
bag_map = [[False for j in range(n + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if products[i - 1] > j:
            bag[i][j] = bag[i - 1][j]
        else:
            bag[i][j] = min(bag[i - 1][j], bag[i - 1][j - products[i - 1]] + products[i - 1])
            if bag[i][j] < c:
                bag[i][j] += b
            else:
                bag[i][j] -= b
            bag_map[i][j] = True
        if bag[i][j] < best_price:
            best_price = bag[i][j]
            best_price_x, best_price_y = i, j

if best_price > a + b:
    best_price = -1

answer = []
i = best_price_x
j = best_price_x

while i > 0:
    if bag_map[i][j]:
        answer.append(i)
        j -= products[i - 1]
        i -= 1
    else:
        i -= 1

print(best_price)
print(*answer)
