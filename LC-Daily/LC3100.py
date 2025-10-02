# https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, b: int, e: int) -> int:
        out = 0
        while b >= e:
            b -= e
            out += e
            b += 1
            e += 1
        return out+b
