# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/

# Approach 1: Priority Queue
# TC: O(N*M*Log(N*M))
class Solution:
    def minCost(self, mat: List[List[int]]) -> int:
        INF = 10**9
        n, m = len(mat), len(mat[0])
        dp = [[INF for j in range(m)]for i in range(n)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        dp[0][0] = 0
        pq = [(0, 0, 0)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while pq:
            c, x, y = heappop(pq)
            if x == n-1 and y == m-1:
                return c
            if dp[x][y] < c:
                continue
            for i in range(4):
                a, b = x+dirs[i][0], y+dirs[i][1]
                if not valid(a, b):
                    continue
                if mat[x][y] == i+1:
                    cc = c
                else:
                    cc = c+1
                if dp[a][b] <= cc:
                    continue
                dp[a][b] = cc
                heappush(pq, (cc, a, b))
        return -1


# Approach 2: Replacing Priority Queue with Deque
# TC: O(N*M)
class Solution:
    def minCost(self, mat: List[List[int]]) -> int:
        INF = 10**9
        n, m = len(mat), len(mat[0])
        dp = [[INF for j in range(m)]for i in range(n)]

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m

        dp[0][0] = 0
        dq = deque([(0, 0, 0)])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            c, x, y = dq.popleft()
            if x == n-1 and y == m-1:
                return c
            if dp[x][y] < c:
                continue
            for i in range(4):
                a, b = x+dirs[i][0], y+dirs[i][1]
                if not valid(a, b):
                    continue
                if mat[x][y] == i+1:
                    cc = c
                else:
                    cc = c+1
                if dp[a][b] <= cc:
                    continue
                dp[a][b] = cc
                if cc == c:
                    dq.appendleft((cc, a, b))
                else:
                    dq.append((cc, a, b))
        return -1
