# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/description/

class Solution:
    def xorAfterQueries(self, arr: List[int], queries: List[List[int]]) -> int:
        mod = 10**9+7
        for l, r, k, v in queries:
            for i in range(l, r+1, k):
                arr[i] *= v
                arr[i] %= mod
        out = 0
        for x in arr:
            out ^= x
        return out
