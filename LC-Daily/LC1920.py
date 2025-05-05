# https://leetcode.com/problems/build-array-from-permutation/description/

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [0 for i in range(n)]
        for i in range(n):
            arr[i] = nums[nums[i]]
        return arr
