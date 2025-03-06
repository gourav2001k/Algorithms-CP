# https://leetcode.com/problems/count-total-number-of-colored-cells/description/

class Solution:
    def coloredCells(self, n: int) -> int:
        dp = [1]
        for i in range(1, n):
            dp.append(dp[i-1]+i*4)
        return dp[n-1]
