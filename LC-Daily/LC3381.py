# https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/description/

class Solution:
    def maxSubarraySum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        MIN = -10**15
        ans = [MIN for i in range(n)]
        x = sum(arr[-k:])
        ans[-k] = x
        for i in range(n-k-1, -1, -1):
            x += arr[i]
            x -= arr[i+k]
            ans[i] = max(x, x+ans[i+k])
        return max(ans)
