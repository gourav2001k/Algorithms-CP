# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/description/

class Solution:
    def numberOfPaths(self, mat: List[List[int]], k: int) -> int:
        n, m = len(mat), len(mat[0])
        dp = [[[0 for x in range(k)]for j in range(m)]for i in range(n)]

        mod = 10**9+7
        z = mat[0][0] % k
        dp[0][0][z] = 1
        x = z
        for i in range(1, n):
            x = (x+mat[i][0]) % k
            dp[i][0][x] = 1
        x = z
        for j in range(1, m):
            x = (x+mat[0][j]) % k
            dp[0][j][x] = 1
        for i in range(1, n):
            for j in range(1, m):
                for r in range(k):
                    x = (r-mat[i][j]) % k
                    dp[i][j][r] += dp[i-1][j][x]
                    dp[i][j][r] += dp[i][j-1][x]
                    dp[i][j][r] %= mod

        return dp[n-1][m-1][0]
