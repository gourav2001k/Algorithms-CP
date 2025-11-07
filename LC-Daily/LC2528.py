# https://leetcode.com/problems/maximize-the-minimum-powered-city/description/

class Solution:
    def maxPower(self, stations: List[int], rr: int, k: int) -> int:
        n = len(stations)
        prefix = [0 for i in range(n+1)]
        for i, v in enumerate(stations):
            prefix[max(i-rr, 0)] += v
            prefix[min(i+rr+1, n)] -= v

        def good(x):
            need = 0
            pre = [i for i in prefix]
            for i in range(n):
                if need > k:
                    return False
                if i-1 >= 0:
                    pre[i] += pre[i-1]
                extra = max(x-pre[i], 0)
                need += extra
                pre[i] += extra
                pre[min(i+2*rr+1, n)] -= extra
            return need <= k

        l, r = 0, 10**12
        while l+1 < r:
            m = (l+r) >> 1
            if good(m):
                l = m
            else:
                r = m
        return l
