# https://leetcode.com/problems/count-of-interesting-subarrays/description/

class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        n = len(nums)
        out = 0
        count = Counter()
        count[0] = 1
        arr = [1 if nums[i] % mod == k else 0 for i in range(n)]
        for i in range(n):
            if i:
                arr[i] += arr[i-1]
            arr[i] %= mod
            out += count[(arr[i]-k) % mod]
            count[arr[i]] += 1
        return out
