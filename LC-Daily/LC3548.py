# https://leetcode.com/problems/equal-sum-grid-partition-i/

from typing import List


class Solution:
    def canPartitionGrid(self, mat: List[List[int]]) -> bool:
        if self.validate(mat):
            return True
        mat = self.rotateMat(mat)
        if self.validate(mat):
            return True
        mat = self.rotateMat(mat)
        if self.validate(mat):
            return True
        mat = self.rotateMat(mat)
        if self.validate(mat):
            return True
        return False

    def validate(self, mat):
        n, m = len(mat), len(mat[0])
        s = 0
        for i in range(n):
            for j in range(m):
                s += mat[i][j]

        def check(count, cur, x):
            g = 2*cur-s
            if g < 0:
                return False
            if g not in count:
                return False
            if x:
                if m == 1 and mat[0][0] != g and mat[x][0] != g:
                    return False
                return True
            if mat[0][0] == g or mat[0][m-1] == g:
                return True
            return False

        cur = 0
        count = set()
        for i in range(n):
            for j in range(m):
                cur += mat[i][j]
                count.add(mat[i][j])
            if cur << 1 == s:
                return True
            if check(count, cur, i):
                return True

        return False

    def rotateMat(self, mat):
        n, m = len(mat), len(mat[0])
        nMat = [[0 for i in range(n)]for j in range(m)]
        for i in range(n):
            for j in range(m):
                nMat[m-1-j][i] = mat[i][j]
        return nMat
