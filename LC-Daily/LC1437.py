# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = 10**6
        for x in nums:
            if not x:
                prev += 1
                continue
            if prev < k:
                return False
            prev = 0
        return True
