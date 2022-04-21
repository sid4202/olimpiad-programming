class Solution(object):
    def isValidColumn(self, column):
        for i in column:
            if i.isdigit():
                if column.count(i) > 1:
                    return False
        return True

    def isValidRow(self, board, row_num):
        row = []
        for i in range(len(board)):
            if board[i][row_num].isdigit():
                row.append(board[i][row_num])
        return self.isValidColumn(row)

    def isValid3x3Square(self, board, x, y):
        square = []
        for i in range(x,x + 3):
            square.append(board[i][y:y + 3])
        square_values = []
        for column in square:
            for j in column:
                if j.isdigit():
                    square_values.append(j)
        print(self.isValidColumn(square_values))
        return self.isValidColumn(square_values)

    def allColumnsAreValid(self, board):
        for column in board:
            if not self.isValidColumn(column):
                return False
        return True

    def allRowsAreValid(self, board):
        for i in range(len(board)):
            if not self.isValidRow(board, i):
                return False
        return True

    def allSquaresAreValid(self, board):
        for i in range(0,len(board),3):
            for j in range(0,len(board[i]),3):
                if not self.isValid3x3Square(board, i, j):
                    return False
        return True

    def isValidSudoku(self, board):
        return self.allSquaresAreValid(board) & self.allRowsAreValid(board) & self.allColumnsAreValid(board)

solution = Solution()
print(solution.isValidSudoku([[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]))

