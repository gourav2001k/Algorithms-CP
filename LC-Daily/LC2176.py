# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description/

class Solution:
    def countPairs(self, arr: List[int], k: int) -> int:
        out, n = 0, len(arr)
        for i in range(n):
            for j in range(i+1, n):
                if arr[i] != arr[j]:
                    continue
                if not (i*j) % k:
                    out += 1
        return out
