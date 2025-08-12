# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        k = 1
        sset = []
        while k**x <= n:
            sset.append(k**x)
            k += 1
        return self.subsetSumCount(sset, n)

    def subsetSumCount(self, arr: List[int], t: int) -> int:
        n = len(arr)
        mod = 10**9+7
        dp = [[0 for i in range(t+1)]for j in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]
            for j in range(1, t+1):
                dp[i][j] += dp[i-1][j]
                if j >= arr[i-1]:
                    dp[i][j] += dp[i-1][j-arr[i-1]]
                dp[i][j] %= mod
        return dp[n][t]
