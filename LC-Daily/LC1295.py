# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        out = 0
        for x in nums:
            even = 1
            while x:
                even ^= 1
                x //= 10
            out += even
        return out
