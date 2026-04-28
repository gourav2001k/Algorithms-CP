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


# approach 2: flatten sort and take median as target value, then calculate operations
class Solution:
    def minOperations(self, mat: List[List[int]], x: int) -> int:
        arr = []
        for row in mat:
            arr += row
        arr.sort()
        n = len(arr)
        median = arr[(n-1) >> 1]
        out = (median-arr[0])//x
        for i in range(1, n):
            if (arr[i]-arr[i-1]) % x:
                return -1
            out += abs(median-arr[i])//x
        return out
