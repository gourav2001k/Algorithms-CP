# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, arr: List[int]) -> bool:
        n = len(arr)
        mx = 0
        for i in range(n):
            if mx < i:
                break
            mx = max(mx, i+arr[i])
        return mx >= n-1
