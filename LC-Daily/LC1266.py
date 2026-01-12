# https://leetcode.com/problems/minimum-time-visiting-all-points/description/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x, y = points[0]
        out = 0
        for a, b in points:
            out += max(abs(x-a), abs(y-b))
            x, y = a, b
        return out
