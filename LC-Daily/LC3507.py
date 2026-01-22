# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/description

class Solution:
    def minimumPairRemoval(self, arr: List[int]) -> int:
        n = len(arr)
        inc = True
        x, y = -1, -1
        m = 10**9
        for i in range(1, n):
            if arr[i]+arr[i-1] < m:
                m = arr[i]+arr[i-1]
                x, y = i, i-1
            if arr[i] < arr[i-1]:
                inc = False
        if inc:
            return 0
        arr[x] = m
        del arr[y]
        return 1+self.minimumPairRemoval(arr)
