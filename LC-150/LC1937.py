# https://leetcode.com/problems/maximum-number-of-points-with-cost/description/

class Solution:
    def maxPoints(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        def maxArr(arr):
            l = len(arr)
            maxLeft = [arr[0]-(l-1) for i in range(l)]
            maxRight = [arr[-1]-(l-1) for i in range(l)]
            for i in range(1, l):
                maxLeft[i] = max(maxLeft[i-1], arr[i]-(l-1-i))
                maxRight[l-1-i] = max(maxRight[l-i], arr[l-1-i]-(l-1-i))
            return maxLeft, maxRight

        out = mat[0]
        for i in range(1, n):
            mxL, mxR = maxArr(out)
            temp = [0 for i in range(m)]
            for j in range(m):
                temp[j] = max(mxL[j]+m-1-j, mxR[j]+j)+mat[i][j]
            out = temp

        return max(out)
