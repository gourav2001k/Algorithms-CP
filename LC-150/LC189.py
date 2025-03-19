# https://leetcode.com/problems/rotate-array/description

class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        k %= n
        p = n-k
        for i in range(p//2):
            arr[i], arr[p-1-i] = arr[p-1-i], arr[i]
        for i in range(k//2):
            arr[i+p], arr[n-1-i] = arr[n-1-i], arr[i+p]

        for i in range(n//2):
            arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
