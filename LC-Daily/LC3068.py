# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

class Solution:
    def maximumValueSum(self, arr: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(arr)
        d = 10**10
        c, out = 0, 0
        for i in range(n):
            if k ^ arr[i] > arr[i]:
                c += 1
                out += k ^ arr[i]
            else:
                out += arr[i]
            d = min(d, abs((k ^ arr[i])-arr[i]))

        if c & 1:
            out -= d
        return out
