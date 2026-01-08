# https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/

class Solution:
    def maxDotProduct(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        INF = 10**7
        dp = [[-INF for j in range(m+1)]for i in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                c = arr1[i-1]*arr2[j-1]
                dp[i][j] = max(dp[i-1][j-1]+c, c, dp[i-1][j], dp[i][j-1])
        return dp[n][m]
