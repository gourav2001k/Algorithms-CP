# https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(mat), len(mat[0])
        row = [0 for i in range(n)]
        col = [0 for i in range(m)]
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    continue
                row[i] = 1
                col[j] = 1

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    mat[i][j] = 0
