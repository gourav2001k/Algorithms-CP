# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description

class Solution:
    def maximumCandies(self, arr: List[int], k: int) -> int:
        n = len(arr)

        def good(x):
            out = 0
            for i in arr:
                out += i//x
            return out >= k

        l, r = 0, max(arr)+1
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l
