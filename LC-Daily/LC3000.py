# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area, diag = 0, 0
        for a, b in dimensions:
            if a*a+b*b == diag:
                area = max(a*b, area)
            elif a*a+b*b > diag:
                diag = a*a+b*b
                area = a*b
        return area
