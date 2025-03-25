# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x, y = [], []
        for a, b, c, d in rectangles:
            x.append((a, c))
            y.append((b, d))
        x.sort()
        y.sort()

        xx = []
        prev = 0
        for a, b in x:
            if prev <= a:
                xx.append(prev)
            prev = max(b, prev)

        yy = []
        prev = 0
        for a, b in y:
            if prev <= a:
                yy.append(prev)
            prev = max(b, prev)

        if len(xx) > 2 or len(yy) > 2:
            return True
        return False
