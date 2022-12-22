import copy


class Solution:
    def __init__(self):
        self.arr = []
        self.map = []

    def dfs(self, x, y):
        if x > len(self.arr) - 1 or x < 0 or y < 0 or y > len(self.arr[0]) - 1 or self.arr[x][y] == "C" or self.arr[x][y] == "X":
            return

        self.arr[x][y] = "C"
        self.dfs(x + 1, y)
        self.dfs(x, y + 1)
        self.dfs(x, y - 1)
        self.dfs(x - 1, y)

    def colored_to_islands(self, x, y):
        if x > len(self.arr) - 1 or x < 0 or y < 0 or y > len(self.arr[0]) - 1 or self.arr[x][y] == "X":
            return

        self.arr[x][y] = "0"
        self.colored_to_islands(x + 1, y)
        self.colored_to_islands(x, y + 1)
        self.colored_to_islands(x, y - 1)
        self.colored_to_islands(x - 1, y)

    def solve(self, board: List[List[str]]) -> None:
        self.arr = board
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    self.dfs(i, j)

        for i in range(len(self.arr[0])):
            if self.arr[0][i] == "C":
                self.colored_to_islands(0, i)

        for i in range(len(self.arr)):
            if self.arr[i][0] == "C":
                self.colored_to_islands(i, 0)

        for i in range(len(self.arr[0])):
            if self.arr[len(self.arr) - 1][i] == "C":
                self.colored_to_islands(len(self.arr) - 1, i)

        for i in range(len(self.arr)):
            if self.arr[i][len(self.arr) - 1] == "C":
                self.colored_to_islands(i, len(self.arr) - 1)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.arr[i][j] == 'C':
                    self.arr[i][j] = "X"

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = self.arr[i][j]

        return board
