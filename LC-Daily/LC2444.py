# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

class Solution:
    def countSubarrays(self, arr: List[int], minK: int, maxK: int) -> int:
        n = len(arr)
        prev, out = -1, 0
        h1, h2 = -1, -1
        for i in range(n):
            if arr[i] < minK or arr[i] > maxK:
                prev = i
                h1, h2 = -1, -1
                continue
            if arr[i] == minK:
                h1 = i
            if arr[i] == maxK:
                h2 = i
            if h1 != -1 and h2 != -1:
                out += min(h1, h2)-prev
        return out
