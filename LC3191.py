# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/description/

class Solution:
    def minOperations(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        for i in range(n):
            if arr[i]:
                continue
            if i+2 >= n:
                return -1
            arr[i] ^= 1
            arr[i+1] ^= 1
            arr[i+2] ^= 1
            out += 1
        return out
