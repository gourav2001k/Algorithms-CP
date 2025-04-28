# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/description/

class Solution:
    def countSubarrays(self, arr: List[int], k: int) -> int:
        n = len(arr)
        out = 0
        prev, cur = -1, 0
        for i in range(n):
            cur += arr[i]
            while cur*(i-prev) >= k:
                prev += 1
                cur -= arr[prev]
            out += i-prev
        return out
