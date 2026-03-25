# https://leetcode.com/problems/equal-sum-grid-partition-i/

class Solution:
    def canPartitionGrid(self, mat: List[List[int]]) -> bool:
        n, m = len(mat), len(mat[0])
        s = 0
        for i in range(n):
            for j in range(m):
                s += mat[i][j]
        cur = 0
        for i in range(n):
            for j in range(m):
                cur += mat[i][j]
            if cur << 1 == s:
                return True
        cur = 0
        for j in range(m):
            for i in range(n):
                cur += mat[i][j]
            if cur << 1 == s:
                return True
        return False
