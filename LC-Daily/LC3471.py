# https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        out = -1
        if k == len(nums):
            return max(nums)
        if k > 1:
            if c[nums[0]] == 1:
                out = max(out, nums[0])
            if c[nums[-1]] == 1:
                out = max(out, nums[-1])
            return out

        for x in nums:
            if c[x] > 1:
                continue
            out = max(out, x)
        return out
