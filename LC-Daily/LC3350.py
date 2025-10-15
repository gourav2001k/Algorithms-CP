# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

# Approach 1
# Binary Search O(N*LogN)
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


# Approach 2
# Two Pointers O(N)
class Solution:
    def maxIncreasingSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        a, b, out = 1, 0, 0
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                b, a = a, 1
            else:
                a += 1
            out = max(out, min(a, b), a >> 1)
        return out
