# https://leetcode.com/problems/minimum-distance-to-the-target-element/description/

class Solution:
    def getMinDistance(self, arr: List[int], t: int, s: int) -> int:
        n = len(arr)
        out = 2*n
        for i in range(n):
            if arr[i] != t:
                continue
            if abs(i-s) < abs(out-s):
                out = i
        return abs(out-s)
