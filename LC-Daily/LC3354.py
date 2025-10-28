# https://leetcode.com/problems/make-array-elements-equal-to-zero/description/

class Solution:
    def countValidSelections(self, arr: List[int]) -> int:
        n = len(arr)
        pre = [0 for i in range(n+1)]
        s, out = sum(arr), 0
        for i in range(n):
            pre[i+1] += pre[i]+arr[i]
            d = abs(s-2*pre[i+1])
            if arr[i]:
                continue
            if not d:
                out += 2
            elif d == 1:
                out += 1
        return out
