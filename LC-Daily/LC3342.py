# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description

class Solution:
    def minTimeToReach(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        vis = [[0 for i in range(m)]for j in range(n)]

        def verify(a, b):
            return 0 <= a < n and 0 <= b < m

        heap = [(0, 1, 0, 0)]
        vis[0][0] = 1
        dir = [0, 1, 0, -1, 0]
        while heap:
            t, c, x, y = heappop(heap)
            if c > 1:
                nC = 1
            else:
                nC = 2
            if x == n-1 and y == m-1:
                return t
            for i in range(4):
                a, b = x+dir[i], y+dir[i+1]
                if not verify(a, b):
                    continue
                if vis[a][b]:
                    continue
                vis[a][b] = 1
                heappush(heap, (max(t, mat[a][b])+c, nC, a, b))
        return -1
