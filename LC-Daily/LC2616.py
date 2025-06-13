# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/

class Solution:
    def minimizeMax(self, arr: List[int], p: int) -> int:
        n = len(arr)
        arr.sort()
        diff = []
        for i in range(1, n):
            diff.append(arr[i]-arr[i-1])

        def check(x):
            taken, c = False, 0
            for i in range(n-1):
                if taken:
                    taken = False
                    continue
                if diff[i] <= x:
                    taken = True
                    c += 1
            return c >= p

        l, r = -1, 10**9
        while l+1 < r:
            m = (l+r) >> 1
            if check(m):
                r = m
            else:
                l = m
        return r
