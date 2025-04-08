# https://leetcode.com/problems/swim-in-rising-water/description/

# Approach 1: Using Binary Search TC: O(N*M*Log(N*M))
class Solution:
    def swimInWater(self, mat: List[List[int]]) -> int:
        n = len(mat)

        dirs = [0, 1, 0, -1, 0]
        def verify(x, y): return 0 <= x < n and 0 <= y < n

        def good(k):
            if mat[0][0] > k:
                return False
            vis = [[0 for i in range(n)]for j in range(n)]
            vis[0][0] = 1
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == n-1 and y == n-1:
                    return True
                for i in range(4):
                    a, b = x+dirs[i], y+dirs[i+1]
                    if not verify(a, b):
                        continue
                    if vis[a][b]:
                        continue
                    if mat[a][b] > k:
                        continue
                    vis[a][b] = 1
                    q.append((a, b))
            return False

        l, r = -1, n*n
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m
        return r


# Approach 2: Using Heap/Dijkstra TC: O(N*M*Log(N*M))

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
