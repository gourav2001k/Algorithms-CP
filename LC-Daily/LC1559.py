# https://leetcode.com/problems/detect-cycles-in-2d-grid/description/

class Solution:
    def containsCycle(self, mat: List[List[str]]) -> bool:
        n, m = len(mat), len(mat[0])
        vis = [[0 for j in range(m)]for i in range(n)]
        dirs = [0, 1, 0, -1, 0]
        def verify(x, y): return 0 <= x < n and 0 <= y < m

        def dfs(x, y, p=-1, q=-1):
            for i in range(4):
                a, b = dirs[i]+x, dirs[i+1]+y
                if not verify(a, b):
                    continue
                if p == a and q == b:
                    continue
                if mat[x][y] != mat[a][b]:
                    continue
                if vis[a][b]:
                    return True
                vis[a][b] = 1
                if dfs(a, b, x, y):
                    return True
            return False

        for i in range(n):
            for j in range(m):
                if vis[i][j]:
                    continue
                vis[i][j] = 1
                if dfs(i, j):
                    return True

        return False
