# https://leetcode.com/problems/three-consecutive-odds/description/

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] & 1 and arr[i] & 1 and arr[i+1] & 1:
                return True
        return False
