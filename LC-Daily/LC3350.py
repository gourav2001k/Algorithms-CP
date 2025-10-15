# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n
        while l+1 < r:
            m = (l+r) >> 1
            if self.hasIncreasingSubarrays(nums, m):
                l = m
            else:
                r = m
        return l

    def hasIncreasingSubarrays(self, arr: List[int], k: int) -> bool:
        n = len(arr)
        out = [1 for i in range(n)]
        for i in range(n-2, -1, -1):
            if arr[i] >= arr[i+1]:
                continue
            out[i] += out[i+1]

        for i in range(n-2*k+1):
            if out[i] >= k and out[i+k] >= k:
                return True
        return False
