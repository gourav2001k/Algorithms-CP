# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        n = len(arr)
        prefix = [1 for i in range(n)]
        suffix = [1 for i in range(n)]
        prefix[0], suffix[n-1] = arr[0], arr[n-1]
        for i in range(1, n):
            prefix[i] = prefix[i-1]*arr[i]
            suffix[n-1-i] = suffix[n-i]*arr[n-1-i]

        out = [0 for i in range(n)]
        out[0], out[n-1] = suffix[1], prefix[n-2]
        for i in range(1, n-1):
            out[i] = prefix[i-1]*suffix[i+1]
        return out
