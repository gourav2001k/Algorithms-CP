# https://leetcode.com/problems/minimum-time-difference/description/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        arr = list(sorted(map(self.convertToMinutes, timePoints)))
        MAX_MINS = 60*24
        out = MAX_MINS
        for i in range(n):
            out = min(out, (arr[i]-arr[i-1]) % MAX_MINS)
        return out

    def convertToMinutes(self, time):
        hrs, mins = map(int, time.split(':'))
        return hrs*60+mins
