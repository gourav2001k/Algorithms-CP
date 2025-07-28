# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/description/

class Solution:
    def smallestSubarrays(self, arr: List[int]) -> List[int]:
        n, x = len(arr), 0
        out = [0 for i in range(n)]
        bits = [0 for i in range(32)]
        for i in range(n-1, -1, -1):
            x |= arr[i]
            for j in range(32):
                if (1 << j) & arr[i]:
                    bits[j] = i
            if not x:
                out[i] = 1
            else:
                out[i] = 1+max(bits)-i
        return out
