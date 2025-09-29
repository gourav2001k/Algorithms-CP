# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/

class Solution:
    def minScoreTriangulation(self, arr: List[int]) -> int:
        dp = dict()

        def solve(i, j):
            key = (i, j)
            if key in dp:
                return dp[key]
            if j-i < 2:
                return 0
            out = 10**9
            for k in range(i+1, j):
                out = min(out, solve(i, k)+solve(k, j)+arr[i]*arr[j]*arr[k])
            dp[key] = out
            return out
        return solve(0, len(arr)-1)
