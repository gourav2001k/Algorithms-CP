# https://leetcode.com/problems/minimum-removals-to-balance-array/description/?

class Solution:
    def minRemoval(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr.sort()

        def good(x):
            xx = n-1-x
            for i in range(xx, n):
                if arr[i] <= k*arr[i-xx]:
                    return True
            return False

        l, r = -1, n
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m
        return r
