# https://leetcode.com/problems/find-triangular-sum-of-an-array

class Solution:
    def triangularSum(self, arr: List[int]) -> int:
        while len(arr) > 1:
            temp = []
            for i in range(1, len(arr)):
                temp.append((arr[i]+arr[i-1]) % 10)
            arr = temp
        return arr[0]
