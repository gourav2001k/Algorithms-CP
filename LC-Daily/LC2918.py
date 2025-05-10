# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/description/

class Solution:
    def minSum(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        s1, s2 = sum(arr1), sum(arr2)
        z1, z2 = arr1.count(0), arr2.count(0)
        if s1+z1 == s2+z2:
            return s2+z2
        if s2+z2 < s1+z1:
            s1, z1, s2, z2 = s2, z2, s1, z1
        if z1 == 0:
            return -1
        return s2+z2
