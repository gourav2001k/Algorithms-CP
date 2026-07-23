# https://leetcode.com/problems/number-of-unique-xor-triplets-i/description/

class Solution:
    def uniqueXorTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return n
        mx = 0
        while n:
            n >>= 1
            mx += 1
        return 1 << mx
