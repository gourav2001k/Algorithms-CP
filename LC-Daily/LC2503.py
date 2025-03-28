# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/description

class Solution:
    def maxPoints(self, mat: List[List[int]], queries: List[int]) -> List[int]:
        n, m = len(mat), len(mat[0])
        vis = [[0 for i in range(m)]for j in range(n)]
        pq = [(mat[0][0], 0, 0)]
        vis[0][0] = 1

        def verify(x, y):
            return 0 <= x < n and 0 <= y < m

        k = len(queries)
        out = [0 for i in range(k)]
        dirs = [0, -1, 0, 1, 0]
        qq = list(enumerate(queries))
        qq.sort(key=lambda x: (x[1], x[0]))

        t = 0
        for i in range(k):
            idx, q = qq[i]
            while pq and pq[0][0] < q:
                cur, x, y = heappop(pq)
                t += 1
                for j in range(4):
                    a, b = x+dirs[j], y+dirs[j+1]
                    if not verify(a, b):
                        continue
                    if vis[a][b]:
                        continue
                    vis[a][b] = 1
                    heappush(pq, (mat[a][b], a, b))
            out[idx] += t
        return out
