# https://leetcode.com/problems/shortest-common-supersequence/description/

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        n, m = len(a), len(b)

        # LCS DP precompute
        dp = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0]
            for j in range(1, m+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if a[i-1] != b[j-1]:
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

        x, y = n, m
        out = ''
        # retrace to add common and non common to make supersequence
        while x and y:
            if dp[x-1][y] == dp[x][y]:
                out += a[x-1]
                x -= 1
            elif dp[x][y-1] == dp[x][y]:
                out += b[y-1]
                y -= 1
            else:
                out += a[x-1]
                x -= 1
                y -= 1

        while x:
            out += a[x-1]
            x -= 1
        while y:
            out += b[y-1]
            y -= 1

        return out[::-1]
