# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/submissions

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[1])
        dp = [0 for i in range(n+1)]
        for _ in range(k):
            nDp = [0 for i in range(n+1)]
            for i in range(n):
                nDp[i+1] = max(dp[i+1], nDp[i])
                idx = self.bisect(events, events[i][0])
                nDp[i+1] = max(nDp[i+1], dp[idx+1]+events[i][2])
            dp = nDp
        return dp[n]

    def bisect(self, events, x):
        n = len(events)
        l, r = -1, n
        while l+1 < r:
            m = (l+r) >> 1
            if events[m][1] < x:
                l = m
            else:
                r = m
        return l
