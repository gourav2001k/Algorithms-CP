# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/description/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = sorted(set(nums))
        if k > arr[0]:
            return -1
        if k == arr[0]:
            return len(arr)-1
        return len(arr)
