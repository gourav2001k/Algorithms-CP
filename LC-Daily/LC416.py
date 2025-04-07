# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        n = len(arr)
        t = sum(arr)
        if t & 1:
            return False
        t >>= 1
        dp = [0 for j in range(t+1)]
        dp[0] = 1
        for i in range(1, n+1):
            nDp = [0 for i in range(t+1)]
            nDp[0] = dp[0]
            for j in range(1, t+1):
                nDp[j] = dp[j]
                if j-arr[i-1] < 0:
                    continue
                nDp[j] |= dp[j-arr[i-1]]
            dp = nDp

        if dp[t]:
            return True
        return False
