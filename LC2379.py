# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description

class Solution:
    def minimumRecolors(self, s: str, k: int) -> int:
        n = len(s)
        w, out = 0, 0
        for i in range(k):
            if s[i] == 'W':
                w += 1
        out = w
        for i in range(k, n):
            if s[i-k] == 'W':
                w -= 1
            if s[i] == 'W':
                w += 1
            out = min(out, w)
        return out
