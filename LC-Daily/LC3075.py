# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/

class Solution:
    def maximumHappinessSum(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr.sort(reverse=True)
        out = 0
        for i in range(k):
            out += max(0, arr[i]-i)
        return out
