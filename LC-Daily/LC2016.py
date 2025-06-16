# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/

class Solution:
    def maximumDifference(self, arr: List[int]) -> int:
        n = len(arr)
        mx = arr[n-1]
        out = -1
        for i in range(n-2, -1, -1):
            if mx > arr[i]:
                out = max(out, mx-arr[i])
            else:
                mx = arr[i]
        return out
