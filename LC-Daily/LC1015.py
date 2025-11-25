# https://leetcode.com/problems/smallest-integer-divisible-by-k/description/

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        r, p = 1, 1
        out = 1
        s = set()
        while r:
            r %= k
            if not r:
                return out
            if r in s:
                return -1
            s.add(r)
            out += 1
            p *= 10
            p %= k
            r += p
