# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/description

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        left = [[0, 0, 0]for i in range(n)]
        count, mask, cur = 0, 0, 0
        for i in range(n-1):
            b = 1 << (ord(s[i])-97)
            if not mask & b:
                cur += 1
                mask |= b
            if cur > k:
                count += 1
                mask = b
                cur = 1
            left[i+1] = [count, mask, cur]

        right = [[0, 0, 0] for i in range(n)]
        count, mask, cur = 0, 0, 0
        for i in range(n-1, 0, -1):
            b = 1 << (ord(s[i])-97)
            if not mask & b:
                cur += 1
                mask |= b
            if cur > k:
                count += 1
                mask = b
                cur = 1
            right[i-1] = [count, mask, cur]

        out = 0
        for i in range(n):
            t = left[i][0]+right[i][0]+2
            mask = left[i][1] | right[i][1]
            b = self.countBits(mask)
            if left[i][2] == k and right[i][2] == k and b < 26:
                t += 1
            elif min(b+1, 26) <= k:
                t -= 1
            out = max(out, t)
        return out

    def countBits(self, x):
        b = 0
        while x:
            b += 1
            x &= x-1
        return b
