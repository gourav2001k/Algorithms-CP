# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        c, out = 0, 0
        mod = 10**9+7
        for i in range(n):
            if s[i] == '1':
                c += 1
            else:
                out += (c*(c+1)) >> 1
                out %= mod
                c = 0
        out += (c*(c+1)) >> 1
        out %= mod
        return out
