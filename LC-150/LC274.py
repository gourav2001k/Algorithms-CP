# https://leetcode.com/problems/h-index/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        def good(x):
            c = 0
            for citeCount in citations:
                if citeCount >= x:
                    c += 1
            return c >= x

        l, r = 0, n+1
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l
