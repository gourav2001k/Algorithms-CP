# https://leetcode.com/problems/count-the-number-of-fair-pairs/description

class Solution:
    def countFairPairs(self, arr: List[int], l: int, r: int) -> int:
        n = len(arr)
        arr.sort()
        out = 0
        for i in range(n):
            x, y = l-arr[i], r-arr[i]
            p = max(i+1, bisect_left(arr, x))
            q = max(i+1, bisect_right(arr, y))
            out += q-p
        return out
