# https://leetcode.com/problems/valid-sudoku/description/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        block = defaultdict(set)
        try:
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
            return True
        except:
            return False
