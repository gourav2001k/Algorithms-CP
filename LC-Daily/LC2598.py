# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations

class Solution:
    def findSmallestInteger(self, arr: List[int], v: int) -> int:
        arr.sort(reverse=True)
        buckets = [0 for i in range(v)]
        for x in arr:
            buckets[x % v] += 1

        mex = 0
        while buckets[mex % v]:
            buckets[mex % v] -= 1
            mex += 1
        return mex
