# https://leetcode.com/problems/longest-balanced-subarray-i/description/

class Solution:
    def longestBalanced(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        for i in range(n):
            distinct, odd = set(), set()
            for j in range(i, n):
                if arr[j] & 1:
                    odd.add(arr[j])
                distinct.add(arr[j])
                if len(distinct) == len(odd) << 1:
                    out = max(out, j-i+1)
        return out
