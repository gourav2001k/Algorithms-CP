# https://leetcode.com/problems/number-of-closed-islands/description/

class Solution:
    def closedIsland(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])

        vis = [[0 for j in range(m)]for i in range(m)]
        dirs = [0, -1, 0, 1, 0]

        def verify(x, y):
            return 0 <= x < n and 0 <= y < m

        def nonBoundary(x, y):
            for i in range(4):
                a, b = x+dirs[i], y+dirs[i+1]
                if not verify(a, b):
                    return 0
            return 1

        def check(x, y):
            vis[x][y] = 1
            pos = nonBoundary(x, y)
            for i in range(4):
                a, b = x+dirs[i], y+dirs[i+1]
                if not verify(a, b):
                    continue
                if vis[a][b]:
                    continue
                if mat[a][b]:
                    continue
                if not check(a, b):
                    pos = 0
            return pos

        out = 0
        for i in range(n):
            for j in range(m):
                if vis[i][j]:
                    continue
                if mat[i][j]:
                    continue
                if check(i, j):
                    out += 1
        return out
