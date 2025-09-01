# https://leetcode.com/problems/maximum-average-pass-ratio/description/

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], k: int) -> float:
        heap = []
        for p, t in classes:
            heappush(heap, ((p/t)-(p+1)/(t+1), p, t))

        x = 0
        while k and heap:
            r, p, t = heappop(heap)
            t += 1
            p += 1
            heappush(heap, ((p/t)-(p+1)/(t+1), p, t))
            k -= 1

        out, d = 0, 0
        while heap:
            r, p, t = heappop(heap)
            out += p/t
            d += 1

        return out/d
