# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/

# Binary Search Approach
class Solution:
    def maxAbsoluteSum(self, arr: List[int]) -> int:
        n = len(arr)

        def good(x):
            cur = 0
            mx, mn = 0, 0
            for i in range(n):
                cur += arr[i]
                if cur-mn >= x:
                    return True
                if mx-cur >= x:
                    return True
                mx = max(mx, cur)
                mn = min(mn, cur)
            return False

        l, r = 0, 10**9+1
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l
