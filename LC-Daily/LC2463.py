# https://leetcode.com/problems/minimum-total-distance-traveled/description/

class Solution:
    def minimumTotalDistance(self, robots: List[int], factory: List[List[int]]) -> int:
        facs = []
        for loc, count in factory:
            for _ in range(count):
                facs.append(loc)
        facs.sort()
        robots.sort()

        MX = 10**18
        n, m = len(robots), len(facs)
        dp = [[MX for j in range(m+1)]for i in range(n+1)]
        for i in range(m+1):
            dp[0][i] = 0
        for i in range(n):
            for j in range(i, m):
                dp[i+1][j+1] = min(dp[i][j]+abs(facs[j]-robots[i]), dp[i+1][j])
        return dp[n][m]
