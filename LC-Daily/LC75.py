# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        a, b = -1, -1
        for i in range(n):
            if arr[i] == 2:
                continue
            elif arr[i] == 1:
                b += 1
                arr[b], arr[i] = arr[i], arr[b]
            else:
                a += 1
                b += 1
                arr[b], arr[i] = arr[i], arr[b]
                arr[a], arr[b] = arr[b], arr[a]
