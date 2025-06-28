# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

class Solution:
    def numSubseq(self, arr: List[int], t: int) -> int:
        n = len(arr)
        arr.sort()
        out, mod = 0, 10**9+7
        for i in range(n):
            if arr[i] >= t:
                continue
            diff = t-arr[i]
            if diff < arr[i]:
                continue
            idx = bisect_right(arr, diff)
            out += pow(2, idx-i-1, mod)
            out %= mod
        return out
