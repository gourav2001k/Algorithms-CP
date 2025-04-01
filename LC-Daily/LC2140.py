# https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp = [0 for i in range(n)]
        for i in range(n-1, -1, -1):
            dp[i] = arr[i][0]
            if arr[i][1]+i+1 < n:
                dp[i] += dp[arr[i][1]+i+1]
            if i+1 < n:
                dp[i] = max(dp[i], dp[i+1])
        return dp[0]
