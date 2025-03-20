# https://leetcode.com/problems/h-index/description/

# Approach 1: Binary Search, TC : O(N*Log(N))
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


# Approach 2: Bucket/Counting, TC : O(N)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counts = [0 for i in range(n+1)]
        for c in citations:
            if c >= n:
                counts[n] += 1
            else:
                counts[c] += 1
        t = 0
        for i in range(n, -1, -1):
            t += counts[i]
            if t >= i:
                return i
