# https://leetcode.com/problems/twisted-mirror-path-count/

class Solution:
    def uniquePaths(self, mat: List[List[int]]) -> int:
        mod = 10**9+7
        n, m = len(mat), len(mat[0])

        @lru_cache(None)
        def solve(x, y, a, b):
            out = 0
            if x >= n or y >= m:
                return out
            if x == n-1 and y == m-1:
                return out+1
            if mat[x][y] == 1:
                if x == a:
                    return solve(x+1, y, x, y)
                if y == b:
                    return solve(x, y+1, x, y)
            out += solve(x+1, y, x, y)
            out += solve(x, y+1, x, y)
            return out % mod

        return solve(0, 0, -1, -1)
