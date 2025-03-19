# https://leetcode.com/problems/minimum-time-to-repair-cars/description/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def good(x):
            t = 0
            for r in ranks:
                t += floor((x/r)**0.5)
            return t >= cars

        l, r = 0, 10**15
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m
        return r
