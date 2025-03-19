# https://leetcode.com/problems/house-robber-iv/description/

class Solution:
    def minCapability(self, arr: List[int], k: int) -> int:
        n = len(arr)
        l, r = min(arr)-1, max(arr)+1

        def good(x):
            c, p = 0, -2
            for i in range(n):
                if arr[i] > x:
                    continue
                if p+1 == i:
                    continue
                p = i
                c += 1
            return c >= k

        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m

        return r
