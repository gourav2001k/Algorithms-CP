# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
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
