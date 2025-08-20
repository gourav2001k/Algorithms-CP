# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0 for i in range(m+1)]for j in range(n+1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i+1][j]+pre[i][j+1]-pre[i][j]+mat[i][j]

        def tot(x1, y1, x2, y2):
            return pre[x2+1][y2+1]-pre[x2+1][y1]-pre[x1][y2+1]+pre[x1][y1]

        out = 0
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    continue
                k = 0
                while i+k < n and j+k < m and tot(i, j, i+k, j+k) == (k+1)**2:
                    k += 1
                out += k

        return out
