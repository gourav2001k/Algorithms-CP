# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/description

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n, p = 0, 0
        for i in nums:
            if i < 0:
                n += 1
            elif i > 0:
                p += 1
        return max(n, p)
