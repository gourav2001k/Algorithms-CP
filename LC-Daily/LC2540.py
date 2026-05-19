# https://leetcode.com/problems/minimum-common-value/description/

class Solution:
    def getCommon(self, arr1: List[int], arr2: List[int]) -> int:
        n, m = len(arr1), len(arr2)
        arr1.sort()
        arr2.sort()

        i, j = 0, 0
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:
                j += 1
            else:
                return arr1[i]
        return -1
