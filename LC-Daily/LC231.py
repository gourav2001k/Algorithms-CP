# https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(32):
            if 1 << i == n:
                return True
        return False
