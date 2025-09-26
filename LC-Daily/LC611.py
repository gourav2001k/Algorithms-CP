# https://leetcode.com/problems/valid-triangle-number/description/

class Solution:
    def triangleNumber(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        out = 0
        for i in range(n):
            for j in range(i+1, n):
                x = arr[i]+arr[j]
                k = bisect_left(arr, x)
                out += max(0, k-j-1)
        return out
