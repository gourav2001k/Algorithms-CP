# https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, arr: list[int]) -> bool:
        n = len(arr)
        odds = []
        for x in arr:
            if x & 1:
                odds.append(x)
        odds.sort()
        out = 3  # 11 in binary
        for i in range(n):
            t = 0
            if arr[i] & 1:
                t |= 1
                if odds and arr[i]-odds[0] >= 1:
                    t |= 1 << 1
            else:
                t |= 1 << 1
                if odds and arr[i]-odds[0] >= 1:
                    t |= 1
            out &= t

        return bool(out)
