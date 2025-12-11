# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/description/

class Solution:
    def countPermutations(self, arr: List[int]) -> int:
        n = len(arr)
        root = arr[0]
        out, mod = 1, 10**9+7
        for i in range(1, n):
            if arr[i] <= root:
                return 0
            out *= i
            out %= mod
        return out
