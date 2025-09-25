# https://leetcode.com/problems/triangle/description/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        minPath = triangle[0]
        for i in range(1, len(triangle)):
            nPath = []
            for j in range(len(triangle[i])):
                if i == j:
                    m = minPath[j-1]
                else:
                    m = minPath[j]
                if j:
                    m = min(m, minPath[j-1])
                nPath.append(triangle[i][j]+m)
            minPath = nPath
        return min(minPath)
