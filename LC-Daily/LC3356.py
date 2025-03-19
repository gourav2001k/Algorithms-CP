# https://leetcode.com/problems/zero-array-transformation-ii/description/

class Solution:
    def minZeroArray(self, arr: List[int], queries: List[List[int]]) -> int:
        n, k = len(arr), len(queries)

        def good(x):
            pre = [0 for i in range(n+1)]
            for i in range(x):
                a, b, c = queries[i]
                pre[a] += c
                pre[b+1] -= c

            for i in range(n):
                pre[i+1] += pre[i]
                if pre[i] < arr[i]:
                    return False
            return True

        if not good(k):
            return -1
        l, r = -1, k
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                r = m
            else:
                l = m
        return r
