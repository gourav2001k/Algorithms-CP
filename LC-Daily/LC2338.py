# https://leetcode.com/problems/count-the-number-of-ideal-arrays/description/

class Solution:
    def idealArrays(self, n: int, mex: int) -> int:
        mod = 10**9+7
        m = min(n, 14)
        dp = [[0 for i in range(m+1)]for j in range(mex+1)]
        for i in range(1, mex+1):
            dp[i][1] = 1
            j = 2
            while i*j <= mex:
                for k in range(1, m):
                    dp[i*j][k+1] += dp[i][k]
                j += 1

        fac = [1 for i in range(n)]
        for i in range(1, n):
            fac[i] = (fac[i-1]*i) % mod
        inv = [1 for i in range(n)]
        inv[n-1] = pow(fac[n-1], mod-2, mod)
        for i in range(n-2, -1, -1):
            inv[i] = (inv[i+1]*(i+1)) % mod

        out = 0
        for i in range(1, mex+1):
            for k in range(1, m+1):
                out += dp[i][k]*fac[n-1]*inv[k-1]*inv[n-k]
                out %= mod
        return out
