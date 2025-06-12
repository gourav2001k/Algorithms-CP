# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/

class Solution:
    def maxAdjacentDistance(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        for i in range(n):
            out = max(out, abs(arr[i]-arr[i-1]))
        return out
