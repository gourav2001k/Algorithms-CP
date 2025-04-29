# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

class Solution:
    def countSubarrays(self, arr: List[int], k: int) -> int:
        n = len(arr)
        m = max(arr)
        count = Counter()
        prev, out = -1, 0
        for i in range(n):
            count[arr[i]] += 1
            while count[m] >= k:
                out += n-i
                prev += 1
                count[arr[prev]] -= 1
        return out
