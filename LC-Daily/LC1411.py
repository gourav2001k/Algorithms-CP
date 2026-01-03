# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/

class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        dp = [1 for i in range(12)]
        ways = [[0, 1, 0], [0, 1, 2], [0, 2, 0], [0, 2, 1],
                [1, 0, 1], [1, 0, 2], [1, 2, 0], [1, 2, 1],
                [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 2]]

        def isMatch(way1, way2):
            if way1[0] == way2[0]:
                return True
            if way1[1] == way2[1]:
                return True
            if way1[2] == way2[2]:
                return True
            return False

        for _ in range(1, n):
            nDp = [0 for i in range(12)]
            for i in range(12):
                for j in range(12):
                    if isMatch(ways[i], ways[j]):
                        continue
                    nDp[j] += dp[i]
                    nDp[j] %= mod
            dp = nDp

        out = 0
        for x in dp:
            out += x
            out %= mod
        return out
