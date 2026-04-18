# https://leetcode.com/problems/mirror-distance-of-an-integer/description/

class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(n-self.reverse(n))

    def reverse(self, n: int) -> int:
        x = 0
        while n:
            x *= 10
            x += n % 10
            n //= 10
        return x
