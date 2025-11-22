# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0
        for x in nums:
            if x % 3:
                out += 1
        return out
