# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description

class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        s = set(nums)
        while o in s:
            o <<= 1
        return o
