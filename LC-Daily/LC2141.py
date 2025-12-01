# https://leetcode.com/problems/maximum-running-time-of-n-computers/description/

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def good(x):
            out = 0
            for i in batteries:
                out += min(i, x)
            return (out//x) >= n

        l, r = 0, 10**14+1
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l
