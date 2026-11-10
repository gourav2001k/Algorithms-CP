# https://leetcode.com/problems/climbing-stairs-ii/description/

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        MX = 10**9
        dp = [MX for i in range(n+1)]
        dp[0] = 0
        for i in range(n):
            if i+1 <= n:
                dp[i+1] = min(dp[i+1], dp[i]+1**2+costs[i])
            if i+2 <= n:
                dp[i+2] = min(dp[i+2], dp[i]+2**2+costs[i+1])
            if i+3 <= n:
                dp[i+3] = min(dp[i+3], dp[i]+3**2+costs[i+2])
        return dp[n]
