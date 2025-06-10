# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/

class Solution:
    def maxDifference(self, s: str) -> int:
        n = len(s)
        o, e = 0, n
        c = Counter(s)
        for i in c:
            if c[i] & 1:
                o = max(o, c[i])
            else:
                e = min(e, c[i])
        return o-e
