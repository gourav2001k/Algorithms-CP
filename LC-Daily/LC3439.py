# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description/

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        arr = []
        arr.append(startTime[0])
        for i in range(1, n):
            arr.append(startTime[i]-endTime[i-1])
        arr.append(eventTime-endTime[n-1])

        cur = 0
        for i in range(k+1):
            cur += arr[i]
        out = cur
        for i in range(k+1, len(arr)):
            cur -= arr[i-k-1]
            cur += arr[i]
            out = max(out, cur)
        return out
