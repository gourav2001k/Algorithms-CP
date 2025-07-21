# https://leetcode.com/problems/maximum-erasure-value/description/

class Solution:
    def maximumUniqueSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        last = dict()
        out = 0
        prev, curSum = 0, 0
        for i in range(n):
            if arr[i] in last:
                x = last[arr[i]]
                while prev <= x:
                    curSum -= arr[prev]
                    if arr[prev] in last and last[arr[prev]] == prev:
                        del last[arr[prev]]
                    prev += 1
            last[arr[i]] = i
            curSum += arr[i]
            out = max(out, curSum)
        return out
