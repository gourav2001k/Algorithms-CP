# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

class Solution:
    def maximumLength(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[0 for i in range(k)]for j in range(k)]
        out = 0
        for i in range(n):
            x = arr[i] % k
            for j in range(k):
                prev = (j-x) % k
                dp[x][j] = max(dp[x][j], dp[prev][j]+1)
                out = max(out, dp[x][j])
        return out
