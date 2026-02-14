# https://leetcode.com/problems/champagne-tower/description/

class Solution:
    def champagneTower(self, p: int, r: int, c: int) -> float:
        row = 0
        glasses = [p]
        while row < r:
            n = len(glasses)
            nxt_glasses = [0 for i in range(n+1)]
            for i in range(n):
                if glasses[i] <= 1:
                    continue
                glasses[i] -= 1
                nxt_glasses[i] += glasses[i]/2
                nxt_glasses[i+1] += glasses[i]/2
            glasses = nxt_glasses
            row += 1
        return min(glasses[c], 1)
