n = int(input())
m = int(input())

board = []
for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

board_price = [[None for j in range(m)] for i in range(n)]

def get_price(x, y):
    if x == 0 and y == 0:
        return 0

    if board_price[x][y] is not None:
        return board_price[x][y]

    if x == 0:
        board_price[x][y] = board[x][y] + get_price(x, y - 1)

    elif y == 0:
        board_price[x][y] = board[x][y] + get_price(x - 1, y)

    else:
        board_price[x][y] = board[x][y] + min(get_price(x - 1, y), get_price(x, y - 1))

    return board_price[x][y]


print(get_price(n - 1, m - 1))
