# https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        x, y = 0, 0
        for i in range(1, n+1):
            if i % m:
                x += i
            else:
                y += i
        return x-y
