# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = [0 for i in range(n+1)]
        for i in range(n-1, -1, -1):
            pts, brainPwr = arr[i]
            dp[i] = pts+dp[min(brainPwr+i+1, n)]
            dp[i] = max(dp[i], dp[i+1])
        return dp[0]
