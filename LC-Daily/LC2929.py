# https://leetcode.com/problems/distribute-candies-among-children-ii/description

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        twoWay = [0 for i in range(n+1)]
        for x in range(n+1):
            if 2*limit < x:
                twoWay[x] = 0
            elif x <= limit:
                twoWay[x] = x+1
            else:
                twoWay[x] = 2*limit-x+1

        out = 0
        for x in range(min(n, limit)+1):
            out += twoWay[n-x]
        return out
