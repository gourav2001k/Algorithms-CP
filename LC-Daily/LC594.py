# https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution:
    def findLHS(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        out = 0
        a, b = 0, 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                b += 1
            elif arr[i]-1 == arr[i-1]:
                a = b
                b = 1
            else:
                a = 0
                b = 1
            if a:
                out = max(a+b, out)
        return out
