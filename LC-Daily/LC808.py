# https://leetcode.com/problems/soup-servings/description

class Solution:
    def soupServings(self, n: int) -> float:
        ops = [(100, 0), (75, 25), (50, 50), (25, 75)]
        if n > 4500:
            return 1
        dp = dict()

        def solve(x, y):
            key = (x, y)
            if key in dp:
                return dp[key]
            if x <= 0 and y <= 0:
                return 0.5
            if x <= 0:
                return 1
            if y <= 0:
                return 0
            out = 0
            for a, b in ops:
                out += solve(x-a, y-b)/4
            dp[key] = out
            return out

        return solve(n, n)
