# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/

class Solution:
    def longestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        mx = max(arr)
        out, cur = 0, 0
        for i in range(n):
            if arr[i] != mx:
                cur = 0
                continue
            else:
                cur += 1
            out = max(cur, out)
        return out
