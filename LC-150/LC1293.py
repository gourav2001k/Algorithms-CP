# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description

class Solution:
    def shortestPath(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])

        INF = 10**9
        q = deque([(0, 0, k)])
        vis = [[[INF for i in range(m)] for j in range(n)] for _ in range(k+1)]

        def verify(x, y): return 0 <= x < n and 0 <= y < m

        cost = 0
        vis[k][0][0] = cost
        dirs = [0, 1, 0, -1, 0]
        while q:
            cost += 1
            for _ in range(len(q)):
                x, y, c = q.popleft()
                if x == n-1 and y == m-1:
                    return cost-1
                for i in range(4):
                    a, b = x+dirs[i], y+dirs[i+1]
                    if not verify(a, b):
                        continue
                    if mat[a][b]:
                        if not c:
                            continue
                        if vis[c-1][a][b] != INF:
                            continue
                        vis[c-1][a][b] = cost
                        q.append((a, b, c-1))
                    else:
                        if vis[c][a][b] != INF:
                            continue
                        vis[c][a][b] = cost
                        q.append((a, b, c))
        return -1
