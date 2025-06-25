# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/description/

class Solution:
    def partitionArray(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr.sort()
        out, prev = 0, 0
        for i in range(n):
            if arr[i]-arr[prev] > k:
                out += 1
                prev = i
        return out+1
