# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        o, e, c = 0, 1, 0
        out, mod = 0, 10**9+7
        for i in range(n):
            if arr[i] & 1:
                c ^= 1
            if c:
                out += e
                o += 1
            else:
                out += o
                e += 1
            out %= mod
        return out
