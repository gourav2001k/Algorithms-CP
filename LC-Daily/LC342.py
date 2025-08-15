# https://leetcode.com/problems/power-of-four/description/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        cur = 1
        while cur < n:
            cur <<= 2
        return cur == n
