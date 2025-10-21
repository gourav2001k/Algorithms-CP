# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/description/

class Solution:
    def maxFrequency(self, arr: List[int], k: int, numOperations: int) -> int:
        n = len(arr)
        arr.sort()
        c = Counter(arr)
        MAX = min(arr[-1], 10**5)+1

        out = 0
        for i in range(arr[0], MAX):
            r = bisect_right(arr, i+k)
            l = bisect_left(arr, i-k)
            cur = min(numOperations, r-l-c[i])+c[i]
            out = max(cur, out)
        return out
