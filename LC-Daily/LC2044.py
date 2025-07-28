# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description

class Solution:
    def countMaxOrSubsets(self, arr: List[int]) -> int:
        mx, n = 0, len(arr)
        for i in arr:
            mx |= i

        out = 0
        for i in range(1 << n):
            t = 0
            for j in range(n):
                if i & (1 << j):
                    t |= arr[j]
            out += int(t == mx)
        return out
