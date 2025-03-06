# https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        sm, sqSm = 0, 0
        iSm, iSqSm = ((n**2)*(n**2+1))//2, ((n**2)*(n**2+1)*(2*n**2+1))//6
        for i in range(n):
            for j in range(n):
                sm += mat[i][j]
                sqSm += mat[i][j]**2
        # if x is repeated, y is missing
        xmy = iSm-sm  # ideal sum - element sum = y-x
        xxmyy = iSqSm-sqSm  # ideal sum Sqaure - element sum square = y^2 - x^2
        xpy = xxmyy//xmy  # x+y = (y^2 - x^2)/(y-x)
        # now it's linear equation
        return (xpy-xmy)//2, (xpy+xmy)//2
