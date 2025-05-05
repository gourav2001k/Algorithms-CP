# https://leetcode.com/problems/domino-and-tromino-tiling/description/

class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        dp = [1, 1, 2]
        top, bottom = [0, 0, 1], [0, 0, 1]
        for i in range(3, n+1):
            top.append((bottom[i-1]+dp[i-2]) % mod)
            bottom.append((top[i-1]+dp[i-2]) % mod)
            dp.append((dp[i-2]+dp[i-1]+top[i-1]+bottom[i-1]) % mod)
        return dp[n]
