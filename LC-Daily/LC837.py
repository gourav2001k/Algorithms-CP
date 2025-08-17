# https://leetcode.com/problems/new-21-game/description

class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not k:
            return 1
        dp = [0 for i in range(k+maxPts)]
        s, dp[0] = 1, 1
        for i in range(1, k+maxPts):
            dp[i] += s/maxPts
            if i < k:
                s += dp[i]
            if i-maxPts >= 0:
                s -= dp[i-maxPts]
        return sum(dp[k:n+1])
