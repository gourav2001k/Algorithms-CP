# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description

class Solution:
    def maxEvents(self, arr: List[List[int]]) -> int:
        n = len(arr)
        arr.sort()
        out, c = 0, 1
        heap = []
        for a, b in arr:
            while c < a and heap:
                k = heappop(heap)
                if k >= c:
                    out += 1
                    c += 1
            if c < a:
                c = a
            heappush(heap, b)
        while heap:
            k = heappop(heap)
            if k >= c:
                out += 1
                c += 1
        return out
