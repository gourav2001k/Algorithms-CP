# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        pre = [[0 for j in range(m+1)]for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                pre[i+1][j+1] = pre[i+1][j]+pre[i][j+1]-pre[i][j]+mat[i][j]

        def check(x):
            for i in range(n):
                for j in range(m):
                    if i+x >= n or j+x >= m:
                        continue
                    if self.squareSum(pre, i, j, x) <= threshold:
                        return True
            return False

        l, r = -1, min(n, m)+1
        while l+1 < r:
            x = (l+r) >> 1
            if check(x):
                l = x
            else:
                r = x
        return l+1

    def squareSum(self, pre, x, y, k):
        return pre[x+k+1][y+k+1]-pre[x+k+1][y]-pre[x][y+k+1]+pre[x][y]
