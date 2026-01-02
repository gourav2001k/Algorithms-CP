# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/description/

class Solution:
    def repeatedNTimes(self, arr: List[int]) -> int:
        n = len(arr)
        # since half of them is same,
        # the most spreadout they can be is alternate
        for i in range(1, n):
            if arr[i] == arr[i-1] or arr[i] == arr[i-2]:
                return arr[i]
        return arr[0]
