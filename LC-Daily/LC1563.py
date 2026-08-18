# https://leetcode.com/problems/stone-game-v/description/


class Solution:
    def stoneGameV(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0 for i in range(n+1)]
        for i in range(n):
            pre[i+1] += pre[i]+arr[i]

        @lru_cache(None)
        def solve(i, j):
            out = 0
            if i == j:
                return out
            s = pre[j+1]-pre[i]
            for x in range(i, j):
                c = pre[x+1]-pre[i]
                if c >= s-c:
                    out = max(out, s-c+solve(x+1, j))
                if c <= s-c:
                    out = max(out, c+solve(i, x))
            return out

        return solve(0, n-1)
