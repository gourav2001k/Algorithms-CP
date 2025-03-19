# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        out = 0
        for i in range(n):
            for j in range(i+1, n):
                a, b = arr[i], arr[j]
                k = 2
                while True:
                    c = bisect_left(arr, a+b)
                    if c >= n or arr[c] != a+b:
                        break
                    a, b = b, a+b
                    k += 1
                out = max(out, k)
        if out < 3:
            return 0
        return out
