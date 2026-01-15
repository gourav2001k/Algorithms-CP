# https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/description/

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        hMax, vMax = 2, 2
        c = 1
        for i in range(1, len(hBars)):
            if hBars[i]-1 == hBars[i-1]:
                c += 1
            else:
                c = 1
            hMax = max(hMax, c+1)

        c = 1
        for i in range(1, len(vBars)):
            if vBars[i]-1 == vBars[i-1]:
                c += 1
            else:
                c = 1
            vMax = max(vMax, c+1)

        return min(hMax, vMax)**2
