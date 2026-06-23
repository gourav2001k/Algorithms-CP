# https://leetcode.com/problems/number-of-zigzag-arrays-i/description/

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9+7
        g = r-l+1
        dp = [[g-i-1, i] for i in range(g)]
        l, r = 0, g*(g-1)//2
        for _ in range(3, n+1):
            nDp = [[0, 0] for i in range(g)]
            x = 0
            for i in range(g):
                r = (r-dp[i][1]) % mod
                nDp[i][0] = r
                nDp[i][1] = l
                l = (l+dp[i][0]) % mod
                x = (x+nDp[i][1]) % mod
            dp = nDp
            l, r = 0, x

        out = 0
        for x in dp:
            out += sum(x)
            out %= mod
        return out
