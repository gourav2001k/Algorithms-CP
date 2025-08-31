# https://leetcode.com/problems/sudoku-solver/description/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)
        for i in range(9):
            for j in range(9):
                row[i].add(str(j+1))
                col[i].add(str(j+1))
                block[i].add(str(j+1))
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row[i].remove(board[i][j])
                col[j].remove(board[i][j])
                block[3*(i//3)+j//3].remove(board[i][j])

        def backTrak(i, j):
            if i > 8:
                return True
            x, y = i+1, j+1
            if j == 8:
                y = 0
            else:
                x -= 1
            if board[i][j] != ".":
                return backTrak(x, y)
            for k in range(1, 10):
                if str(k) in row[i] and str(k) in col[j] and str(k) in block[3*(i//3)+j//3]:
                    board[i][j] = str(k)
                    row[i].remove(board[i][j])
                    col[j].remove(board[i][j])
                    block[3*(i//3)+j//3].remove(board[i][j])
                    if backTrak(x, y):
                        return True
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[3*(i//3)+j//3].add(board[i][j])
            board[i][j] = '.'
            return False
        backTrak(0, 0)
