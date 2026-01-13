# https://leetcode.com/problems/separate-squares-i/description/

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        n = len(squares)
        l, r = squares[0][1], squares[0][1]+squares[1][1]
        for i in range(n):
            x, y, s = squares[i]
            l = min(l, y)
            r = max(r, y+s)

        def calculateArea(m):
            a, b = 0, 0
            for i in range(n):
                x, y, s = squares[i]
                y1, y2 = y, y+s
                if m <= y1:
                    b += s*s
                elif m >= y2:
                    a += s*s
                else:
                    a += (m-y1)*s
                    b += (y2-m)*s
            return a, b

        eps = 0.00001
        while r-l > eps:
            m = (l+r)/2
            a, b = calculateArea(m)
            if a < b:
                l = m
            else:
                r = m

        return l
