# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/

class Solution:
    def minMoves(self, arr: list[int]) -> int:
        n = len(arr)
        return sum(arr)-min(arr)*n
