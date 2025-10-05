# https://leetcode.com/problems/pacific-atlantic-water-flow/description

class Solution:
    def pacificAtlantic(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m

        # For pacific ocean
        dp1 = [[0 for i in range(m)] for i in range(n)]
        q = deque([])
        for i in range(n):
            dp1[i][0] = 1  # left border accessible by definition
            q.append((i, 0))
        for i in range(m):
            dp1[0][i] = 1  # Top border accessible by definition
            q.append((0, i))

        q.popleft()  # since 0,0 has been added twice

        while q:
            a, b = q.popleft()
            for x, y in dirs:
                if isValid(a+x, b+y) and not dp1[a+x][b+y] and mat[a+x][b+y] >= mat[a][b]:
                    dp1[a+x][b+y] = 1
                    q.append((a+x, b+y))

        # For atlantic ocean
        dp2 = [[0 for i in range(m)] for i in range(n)]
        q = deque([])
        for i in range(n):
            dp2[i][m-1] = 1  # left border accessible by definition
            q.append((i, m-1))
        for i in range(m):
            dp2[n-1][i] = 1  # Top border accessible by definition
            q.append((n-1, i))

        q.pop()  # since n-1,m-1 has been added twice

        while q:
            a, b = q.popleft()
            for x, y in dirs:
                if isValid(a+x, b+y) and not dp2[a+x][b+y] and mat[a+x][b+y] >= mat[a][b]:
                    dp2[a+x][b+y] = 1
                    q.append((a+x, b+y))

        out = []
        for i in range(n):
            for j in range(m):
                if dp1[i][j] and dp2[i][j]:
                    out.append((i, j))
        return out
