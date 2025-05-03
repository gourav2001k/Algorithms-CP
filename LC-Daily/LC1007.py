# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        x1, y1 = 0, 0
        for i in range(1, n):
            if tops[i] != tops[0]:
                if bottoms[i] == tops[0]:
                    x1 += 1
                else:
                    x1 = n+1
            if bottoms[i] != bottoms[0]:
                if tops[i] == bottoms[0]:
                    y1 += 1
                else:
                    y1 = n+1

        x2, y2 = 1, 1
        tops[0], bottoms[0] = bottoms[0], tops[0]
        for i in range(1, n):
            if tops[i] != tops[0]:
                if bottoms[i] == tops[0]:
                    x2 += 1
                else:
                    x2 = n+1
            if bottoms[i] != bottoms[0]:
                if tops[i] == bottoms[0]:
                    y2 += 1
                else:
                    y2 = n+1

        out = min(x1, y1, x2, y2)
        if out <= n:
            return out
        return -1
