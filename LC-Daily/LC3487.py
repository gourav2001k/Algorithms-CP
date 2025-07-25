# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/description/

class Solution:
    def maxSum(self, arr: List[int]) -> int:
        vis = set()
        out, mx = 0, max(arr)
        for x in arr:
            if x in vis:
                continue
            if x < 0:
                continue
            out += x
            vis.add(x)
        if mx < 0:
            out += mx
        return out
