# https://leetcode.com/problems/trapping-rain-water-ii/description/
# 2D Rain Water Trapping

class Solution:
    def trapRainWater(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        out = 0
        level, heap = 1, []
        vis = [[0 for j in range(m)]for i in range(n)]

        # init boundary for heap, to store boundary
        # top and bottom row
        for i in range(m):
            if not vis[0][i]:
                vis[0][i] = 1
                heappush(heap, (mat[0][i], 0, i))
            if not vis[n-1][i]:
                vis[n-1][i] = 1
                heappush(heap, (mat[n-1][i], n-1, i))
        # left and right column
        for i in range(n):
            if not vis[i][0]:
                vis[i][0] = 1
                heappush(heap, (mat[i][0], i, 0))
            if not vis[i][m-1]:
                vis[i][m-1] = 1
                heappush(heap, (mat[i][m-1], i, m-1))

        def verify(x, y):
            return 0 <= x < n and 0 <= y < m

        dirs = [0, -1, 0, 1, 0]
        while heap:
            if heap[0][0] > level:
                level = heap[0][0]
            h, x, y = heappop(heap)
            for i in range(4):
                a, b = x+dirs[i], y+dirs[i+1]
                if not verify(a, b):
                    continue
                if vis[a][b]:
                    continue
                vis[a][b] = 1
                if mat[a][b] < level:
                    out += level-mat[a][b]
                heappush(heap, (mat[a][b], a, b))

        return out
