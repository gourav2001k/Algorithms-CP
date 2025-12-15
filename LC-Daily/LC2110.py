# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        out, l = 0, 1
        for i in range(1, n):
            if prices[i]+1 == prices[i-1]:
                l += 1
                continue
            out += (l*(l+1)) >> 1
            l = 1
        out += (l*(l+1)) >> 1
        return out
