# https://leetcode.com/problems/jump-game-ii/description

class Solution:
    def jump(self, arr: List[int]) -> int:
        n = len(arr)
        jumps, curEnd, maxEnd = 0, 0, 0
        for i in range(n-1):
            maxEnd = max(maxEnd, arr[i]+i)
            if curEnd != i:
                continue
            curEnd = maxEnd
            jumps += 1
        return jumps
