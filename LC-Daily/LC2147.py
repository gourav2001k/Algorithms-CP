class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9+7
        n, c = len(corridor), 0
        prev, new = 1, 0
        dp = [0 for i in range(n+1)]
        for i in range(n):
            if corridor[i] == "S":
                c += 1
            if c == 2:
                dp[i+1] = prev
                new += prev
                new %= mod
            elif not c:
                dp[i+1] += dp[i]
                new += dp[i]
                new %= mod
            else:
                if new:
                    prev = new
                new = 0
            c, dp[i+1] = c % 2, dp[i+1] % mod
        return dp[n]
