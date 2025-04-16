# https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, arr: List[int], k: int) -> int:
        n = len(arr)
        c = Counter()
        l, r = 0, 0
        out, p = 0, 0
        while r < n and p < k:
            p += c[arr[r]]
            c[arr[r]] += 1
            while p >= k:
                c[arr[l]] -= 1
                p -= c[arr[l]]
                out += n-r
                l += 1
            r += 1
        return out
