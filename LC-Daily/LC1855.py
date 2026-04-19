# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/

from bisect import bisect_left


class Solution:
    def maxDistance(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        arr2.reverse()
        out = 0
        for i in range(n):
            x = bisect_left(arr2, arr1[i])
            out = max(out, m-1-x-i)
        return out
