# https://leetcode.com/problems/power-of-three/description

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        x = 0
        while 3**x <= n:
            if 3**x == n:
                return True
            x += 1
        return False
