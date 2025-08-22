# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/

class Solution:
    def minimumArea(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        xMin, xMax = n, -1
        yMin, yMax = m, -1
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    continue
                xMin = min(xMin, i)
                xMax = max(xMax, i)
                yMin = min(yMin, j)
                yMax = max(yMax, j)
        return (xMax-xMin+1)*(yMax-yMin+1)
