# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/description

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        gaps.append(startTime[0])
        for i in range(1, n):
            gaps.append(startTime[i]-endTime[i-1])
        gaps.append(eventTime-endTime[n-1])

        mex, x = [], gaps[n]
        for i in range(n, -1, -1):
            x = max(x, gaps[i])
            mex.append(x)
        mex.reverse()

        out, l = 0, 0
        for i in range(n):
            g = endTime[i]-startTime[i]
            if g <= l:
                out = max(out, g+gaps[i]+gaps[i+1])
            elif i+2 <= n and g <= mex[i+2]:
                out = max(out, g+gaps[i]+gaps[i+1])
            out = max(out, gaps[i]+gaps[i+1])
            l = max(l, gaps[i])

        return out
