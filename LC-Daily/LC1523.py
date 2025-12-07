# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1:
            low -= 1
        if high & 1:
            high += 1
        return (high-low) >> 1
