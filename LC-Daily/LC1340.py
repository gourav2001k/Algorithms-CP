# https://leetcode.com/problems/jump-game-v/description/

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        out = [-1 for i in range(n)]

        def solve(x):
            if out[x] != -1:
                return
            out[x] = 1
            k = x+1
            while k < n and k-x <= d and arr[k] < arr[x]:
                solve(k)
                out[x] = max(out[x], 1+out[k])
                k += 1
            k = x-1
            while k >= 0 and x-k <= d and arr[k] < arr[x]:
                solve(k)
                out[x] = max(out[x], 1+out[k])
                k -= 1

        for i in range(n):
            solve(i)

        return max(out)
