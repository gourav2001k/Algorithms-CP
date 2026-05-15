# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = -1, n-1
        while l+1 < r:
            m = (l+r) >> 1
            if arr[r] < arr[m]:
                l = m
            else:
                r = m
        return arr[r]
