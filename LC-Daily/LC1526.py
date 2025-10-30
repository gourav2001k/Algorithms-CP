# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/

class Solution:
    def minNumberOperations(self, arr: List[int]) -> int:
        n = len(arr)
        out = arr[0]
        for i in range(1, n):
            out += max(arr[i]-arr[i-1], 0)
        return out
