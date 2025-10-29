# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/

class Solution:
    def smallestNumber(self, n: int) -> int:
        out = 0
        while n:
            out <<= 1
            out |= 1
            n >>= 1
        return out
