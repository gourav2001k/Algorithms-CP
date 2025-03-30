# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description

class Solution:
    def minOperations(self, mat: List[List[int]], x: int) -> int:
        n, m = len(mat), len(mat[0])
        mods = set()
        arr = []
        for i in range(n):
            for j in range(m):
                mods.add(mat[i][j] % x)
                arr.append(mat[i][j])
        if len(mods) > 1:
            return -1
        arr.sort()
        out = 10**9
        s, c = sum(arr), 0
        for i in range(n*m):
            c += arr[i]
            left = (i+1)*arr[i]-c
            right = s - c - (n*m-i-1)*arr[i]
            out = min(out, (left+right)//x)

        return out
