# https://leetcode.com/problems/apply-operations-to-an-array/description/

class Solution:
    def applyOperations(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(1, n):
            if arr[i] != arr[i-1]:
                continue
            arr[i-1] *= 2
            arr[i] = 0

        i, j = 0, 0
        while i < n:
            if arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            i += 1
        return arr
