# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

class Solution:
    def maxFrequency(self, arr: List[int], k: int, numOperations: int) -> int:
        n = len(arr)
        arr.sort()
        c = Counter(arr)
        out = 0
        for i in range(n):
            for x in range(-k, k+1, max(k, 1)):
                r = bisect_right(arr, arr[i]+x+k)
                l = bisect_left(arr, arr[i]+x-k)
                cur = min(numOperations, r-l-c[arr[i]+x])+c[arr[i]+x]
                out = max(cur, out)
        return out
