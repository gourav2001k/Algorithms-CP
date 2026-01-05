class Solution:
    def maxMatrixSum(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        mn = 10**6
        out, c = 0, 0
        for i in range(n):
            for j in range(m):
                out += abs(mat[i][j])
                mn = min(mn, abs(mat[i][j]))
                if mat[i][j] < 0:
                    c ^= 1
        if c:
            out -= 2*mn
        return out
