# https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, arr: list[int], k: int) -> int:
        n = len(arr)
        mins = [arr[i] for i in range(n)]
        for i in range(n-2, -1, -1):
            mins[i] = min(mins[i], mins[i+1])

        mx = arr[0]
        for i in range(n):
            mx = max(arr[i], mx)
            if mx-mins[i] <= k:
                return i

        return -1
