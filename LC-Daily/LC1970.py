# https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution:
    def latestDayToCross(self, n: int, m: int, cells: List[List[int]]) -> int:

        def canCross(mid):
            mat = [[1 for j in range(m)]for i in range(n)]
            for i in range(mid):
                x, y = cells[i]
                mat[x-1][y-1] = 0

            def verify(x, y):
                return 0 <= x < n and 0 <= y < m

            dirs = [0, 1, 0, -1, 0]
            for i in range(m):
                if not mat[0][i]:
                    continue
                mat[0][i] = 0
                q = deque([(0, i)])
                while q:
                    x, y = q.popleft()
                    if x == n-1:
                        return True
                    for j in range(4):
                        a, b = x+dirs[j], y+dirs[j+1]
                        if not verify(a, b):
                            continue
                        if not mat[a][b]:
                            continue
                        mat[a][b] = 0
                        q.append((a, b))
            return False

        l, r = 1, n*m
        while l+1 < r:
            mid = (l+r) >> 1
            if canCross(mid):
                l = mid
            else:
                r = mid
        return l
