# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/description/

class Solution:
    def maximumTripletValue(self, arr: List[int]) -> int:
        n = len(arr)
        bigLeft = [0 for i in range(n)]
        bigRight = [0 for i in range(n)]
        for i in range(1, n):
            bigLeft[i] = max(bigLeft[i-1], arr[i-1])
            bigRight[n-1-i] = max(bigRight[n-i], arr[n-i])

        out = 0
        for i in range(n):
            out = max(out, (bigLeft[i]-arr[i])*bigRight[i])
        return out
