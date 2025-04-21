# https://leetcode.com/problems/count-the-hidden-sequences/description

class Solution:
    def numberOfArrays(self, arr: List[int], lower: int, upper: int) -> int:
        n = len(arr)
        l, r = 0, 0
        cur = 0
        for i in range(n):
            cur += arr[i]
            l = min(l, cur)
            r = max(r, cur)
        return max((upper-lower)-(r-l)+1, 0)
