# https://leetcode.com/problems/water-bottles/submissions/

class Solution:
    def numWaterBottles(self, b: int, e: int) -> int:
        out, l = 0, 0
        while b or l//e:
            out += b
            l += b
            b = l//e
            l %= e
        return out
