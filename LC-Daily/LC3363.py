# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/description/

class Solution:
    def maxCollectedFruits(self, mat: List[List[int]]) -> int:
        n = len(mat)
        out = 0
        for i in range(n):
            # child at (0,0) has no choice other than diagonal
            # to reach (n-1,n-1) in n-1 steps
            out += mat[i][i]

        # now other childs have to take care of thier side of diagonal

        dp = [[0 for i in range(n)]for j in range(n)]
        dp[n-1][0] = mat[n-1][0]
        dp[0][n-1] = mat[0][n-1]
        for i in range(1, n):
            for j in range(i+1):
                if n-1-j > i:
                    dp[n-1-j][i] = max(dp[n-1-j][i-1], dp[n-2-j][i-1])
                    if j:
                        dp[n-1-j][i] = max(dp[n-1-j][i], dp[n-j][i-1])
                    dp[n-1-j][i] += mat[n-1-j][i]
                    dp[i][n-1-j] = max(dp[i-1][n-1-j], dp[i-1][n-2-j])
                    if j:
                        dp[i][n-1-j] = max(dp[i][n-1-j], dp[i-1][n-j])
                    dp[i][n-1-j] += mat[i][n-1-j]

        return out+dp[n-1][n-2]+dp[n-2][n-1]
