# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        n = len(arr)
        prev, c = 1, 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                c += 1
            else:
                c = 1
            if c <= 2:
                arr[prev] = arr[i]
                prev += 1
        return prev
