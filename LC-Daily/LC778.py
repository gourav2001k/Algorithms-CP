# https://leetcode.com/problems/swim-in-rising-water/description/

class Solution:
    def swimInWater(self, mat: List[List[int]]) -> int:
        n = len(mat)

        dirs = [0, 1, 0, -1, 0]
        def verify(x, y): return 0 <= x < n and 0 <= y < n

        pq = [(mat[0][0], 0, 0)]
        vis = [[0 for i in range(n)]for j in range(n)]
        vis[0][0] = 1
        while pq:
            cost, x, y = heappop(pq)
            if x == n-1 and y == n-1:
                return cost
            for i in range(4):
                a, b = x+dirs[i], y+dirs[i+1]
                if not verify(a, b):
                    continue
                if vis[a][b]:
                    continue
                vis[a][b] = 1
                heappush(pq, (max(mat[a][b], cost), a, b))
        return -1
